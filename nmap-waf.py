#!/bin/usr/python3

import sys
import os

print("[+] Checking for WAF...")

ip = sys.argv[1]

def start_nmap(options, ip):
        ip = sys.argv[1]
        command = "nmap" + options + " " + ip
        process = os.popen(command)
        results = str(process.read())
        return results

print (start_nmap(' -p80 --script http-waf-detect', ip))

