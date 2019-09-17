#!/usr/bin/python3

import requests
import sys

useragent = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",}

ip = sys.argv[1]

wplogin= requests.get("http://" + ip + "/wp-login.php")

if wplogin.status_code == 200:

	print("WordPress login page found: PROBABLY WORDPRESS") 
else:
	print("Not Found") 
