#!/bin/usr/python3 

import sys
import nmap
import os 
import requests
import socket

print("[+] Checking for WAF...")

'''
ip = sys.argv[1] 
#Checks if there is WAF on the webserver
nmap1= nmap.PortScanner() 

a = nmap1.nmap_version() 

print(a) 

#takes in the scan and argument 
nm.scan(ip, 
'''

ip = sys.argv[1]
wordlist = sys.argv[2]

'''
def start_nmap(options, ip):
	ip = sys.argv[1]
	command = "nmap" + options + " " + ip
	process = os.popen(command)
	results = str(process.read())
	return results

print (start_nmap(' -p80 --script http-waf-detect', ip))

print ("[+] Checking the target ip ...") 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
	connection = s.connect_ex((ip, 80)) # you can also do socket.connect_ex (check google the difference) 
	s.close() 

	if connection == 0: 
		print (" Finished Checking... ") 
		pass 
	else: 
		print ("Error Occured")
		print ("Error: Couldn't reach target") #just a trouble shoot example 
		sys.exit(1) # timing note check if it gives error for sys.exit 
except socket.error: # socket.error is when the server couldnt connect 
		print ("Error Occured")
		print ("Error: Couldn't reach target") 
		sys.exit(1) 
print ("[+] Checking/Parsing the wordlist") 
'''
try:
	f = open(wordlist)
	wl_check = f.read().strip().split('\n')
	print (" Finished...")

	print (" Amount of Directory path to check: " + (str(len(wl_check)))) # check this 
except IOError: # IOError is an error when input/output is wrong 
	print ("Something went wrong...") 
	sys.exit(1) 

def pathcheck(path): 
	try: 
		response = requests.get("http://" + ip + "/" + path).status_code # makes request to the website using wordlist 
	except Exception:
		print (" Error Occured") 
		#sys.exit(1)
	if response == 200: #If server responds 
		print ("Valid path [200]:" + path ) 
print ("\n Starting Directory Brute Forcing... \n")

for path in (wl_check): 
	pathcheck(path) #check this
print ("\n Scan Complete!") 
'''
except KeyboardInterrupt: 
	print ("\n Interrupted Scan") 
	sys.exit(1) 
'''
