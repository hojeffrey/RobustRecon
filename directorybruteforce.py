#!/bin/usr/python3 

import sys
import os 
import requests

def bruteforce (ip, wordlist):
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

	for path in (wl_check): 
		pathcheck(path) #check this
	print(wl_check)
	print ("\n Scan Complete!") 
