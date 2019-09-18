#!/bin/usr/python3

import sys
import os

print("[+] Checking for WAF...")

# ip = sys.argv[1]


def start_nmap(options, ip):
        # ip = sys.argv[1]
        command = "nmap" + options + " " + ip
        process = os.popen(command)
        results = str(process.read())
        return results


print (start_nmap(' -p80 --script http-waf-detect', ip))

#print (start_nmap(' --script=http-waf-fingerprint', ip))

#print (start_nmap(' --script http-waf-detect.nse', ip))

#print (start_nmap(' -sV -sC -sT -Pn -T4 --script http-waf-detect --script-args=http-waf.detect.detectBodyChanges', ip))
