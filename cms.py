# #!/usr/bin/python3

# import requests
# import sys

       

# # ip = sys.argv[1]
# #useragent = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeb$

# # Making a request to the website to see if it is still online trouble shoot
# def estimate_cms(ip):
#         print("Checking status of the website ...")
#         # WordPress paths
#         wplogin= requests.get("http://" + ip + "/wp-login")

#         if wplogin.status_code == 200 or wplogin.status_code == 301:
#                 print("Detected: Wordpress login (/wp-login)")
#                 print("/n PROBABLY WORDPRESS /n")
#         else:
#                 if wplogin.status_code == 404:
#                 print("Did not detect: Wordpress login (/wp-login)")

#         wpadmin= requests.get("http://" + ip + "/wp-admin")

#         if wpadmin.status_code == 200 or wpadmin.status_code == 301:
#                 print("Detected: Wordpress admin (/wp-admin)")
#                 print("/n PROBABLY WORDPRESS /n")
#         else:
#                 if wplogin.status_code == 404:
#                 print("Did not detect: Wordpress admin (/wp-admin") 

#!/usr/bin/python3

import requests
import sys

       

# ip = sys.argv[1]
#useragent = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeb$

# Making a request to the website to see if it is still online trouble shoot
def estimate_cms(ip):
        print("Checking status of the website ...")
        # WordPress paths
        path_status_pairs = [
                ['/wp-login', 'WORDPRESS'],
                ['/wp-admin', 'WORDPRESS'],
                ['/oogabooga', 'COREY CMS']
        ]

        valid_status_codes = [200, 201, 202, 203, 204, 300, 301, 401, 403]
        
        for pair in path_status_pairs:
                req = requests.get("http://" + ip + pair[0])
                if valid_status_codes.index(req.status_code) != -1: ## == 200 or req.status_code == 301:
                        return pair[1]
        
        return 'UNPREDICTABLE CMS'
