#!/bin/usr/python3 

import sys
import os 
import requests
from colorama import Fore, Style

def bruteforce (ip, wordlist):
	try:
		f = open(wordlist)
		wl_check = f.read().strip().split('\n')
		#print (" Finished...")

		print (" Amount of Directory path to check: " + (str(len(wl_check)))) # check this 
	except IOError: # IOError is an error when input/output is wrong 
		print ("Something went wrong...") 
		sys.exit(1) 
	output = [] 
	def pathcheck(path): 
		valid_status_codes = [200, 201, 202, 203, 204, 300, 301, 302, 304, 401, 403]
		try: 
			response = requests.get("http://" + ip + "/" + path).status_code # makes request to the website using wordlist 
		except Exception:
			print (" Error Occured") 
		#sys.exit(1)
		if response in valid_status_codes: #If server responds 
			return ("Valid path [" + (str(response)) + "] :" + path)
		#else:
			#print (Fore.RED + "Bad path [" + (str(response)) + "] :" + path + Style.RESET_ALL ) 

			
	for path in (wl_check): 
		result = (pathcheck(path))
		if result:
			output.append(result) #check this
	#print(wl_check)
	#print ("\n Scan Complete!")

	return("\n".join(output)) 
if __name__=="__main__":
	brute = bruteforce("192.168.159.130", "wordlist.txt")
	
	print(brute)
