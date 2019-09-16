#!/bin/usr/python3 

import sys
#import nmap
import os 
#import requests
#import socket

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
#wordlist = sys.argv[2]


def start_nmap(options, ip):
        ip = sys.argv[1]
        command = "nmap" + options + " " + ip
        process = os.popen(command)
        results = str(process.read())
        return results

print (start_nmap(' -p80 --script http-waf-detect', ip))

'''
print ("[+] Checking the target ip ..."

try:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except: print("Error")
'''
