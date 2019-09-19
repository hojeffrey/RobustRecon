#!/bin/usr/python3

import os

print("[+] Checking for WAF...")
print("[+] Checking for Crawler...") 

def start_nmap(options, ip):
        command = "nmap" + options + " " + ip
        process = os.popen(command)
        results = str(process.read())
        return results


print (start_nmap(' -p80 --script http-waf-detect', ip))

print (start_nmap(' --script http-sitemap-generator -p 80', ip))

