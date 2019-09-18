#!/usr/bin/python3

import requests
import sys

ip = sys.argv[1]
#useragent = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeb$

# Making a request to the website to see if it is still online trouble shoot
print("Checking status of the website ...")
# WordPress paths
wplogin= requests.get("http://" + ip + "/wp-login")

if wplogin.status_code == 200 or wplogin.status_code == 301:
        print("Detected: Wordpress login (/wp-login)")
        print("/n PROBABLY WORDPRESS /n")
else:
        if wplogin.status_code == 404:
        print("Did not detect: Wordpress login (/wp-login)")

wpadmin= requests.get("http://" + ip + "/wp-admin")

if wpadmin.status_code == 200 or wpadmin.status_code == 301:
        print("Detected: Wordpress admin (/wp-admin)")
        print("/n PROBABLY WORDPRESS /n")
else:
	if wplogin.status_code == 404:
	print("Did not detect: Wordpress admin (/wp-admin") 
