# BeeF-Over-Wan
## Screenshots
![1](https://github.com/Dev913/BeeF-Over-Wan/blob/master/Screenshot%201.png)
![2](https://user-images.githubusercontent.com/33988926/37250458-1b722e3a-2523-11e8-84e4-1e9b4b9f4d02.png)
![3](https://user-images.githubusercontent.com/33988926/37250459-1ba6ad04-2523-11e8-83d8-44549be93735.png)
![4](https://user-images.githubusercontent.com/33988926/37250460-1bdb4e88-2523-11e8-9a0c-20bb7f34d6f7.png)


## Instructions :
You need two Links  which are Forwarded To LocalHost:80 and LocalHost:3000
1. To send to Victim .
2. Beef listens on Port 3000 ,So this link should be forwared to LocalHost:3000 .
	
Just Enter your links in the Script ,Script will do neccessary changes required to opt for your Links .

# NGROK Steps :-
### STEP 1 : Add these Lines To ngrok.yml [Location .ngrok2/ngrok.yml ]
	
	tunnels:
  	first-app:
    	addr: 80
    	proto: http
  	second-app:
    	addr: 3000
    	proto: http
	
### STEP 2 : Now Start ngrok with : 
		ngrok start --all
### STEP 3 : You will See 2 different links Forwarded to
	    Localhost:80                  [ Link To be Sent to Victim ]
        Localhost:3000		  [ Your Link will be Connecting to.. ] 	
						
### STEP 4 : Enter these links in Script and Follow The Steps given in Script.

# Requirements
- Beef-xss [Browser Exploitation Framework] 
- Apache
- NGROK [If you want to do this without Port Forwarding]

## ⭕️ Getting Started
1. ```git clone https://github.com/stormshadow07/BeeF-Over-Wan.git```
2. ```cd BeeF-Over-Wan```
3. ```chmod +x BeeFOverWan.py && python BeeFOverWan.py```
