#!/bin/usr/python3

import os

print("[+] Checking for WAF using wafw00f...")

def start_wafw00f(ip):
        command = "wafw00f" + " " + ip
        process = os.popen(command)
        results = str(process.read())
        return results

