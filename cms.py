#!/usr/bin/python3

import requests 
import sys

def estimate_cms(ip):
	path_pairs = [
		['/wp-login/', '   - PROBABLY WORDPRESS'], 
		['/wp-admin/', '   - PROBABLY WORDPRESS'], 
		['/readme.html','   - PROBABLY WORDPRESS'],
		['/wp-config', '   - PROBABLY WORDPRESS'],
		['/administrator/', '   - PROBABLY Joomla'],
		['/readme.txt', '   - PROBABLY Joomla'],
		['/media/com_joomlaupdate/', '   - PROBABLY Joomla'],
		['/index.php/admin/', '   - PROBABLY Magento'],
		['/RELEASE_NOTES.txt', '   - PROBABLY Magento'],
		['/js/mage/cookies.js', '   - PROBABLY Magento'],
		['/index.php', '   - PROBABLY Magento'],
		['/skin/frontend/default/default/css/styles.css', '   - PROBABLYMagento'],
		['/skin/frontend/default/default/css/styles.css', '   - PROBABLY Magento'],
		['/errors/design.xml', '   - PROBABLYMagento'],
		['/readme.txt', '   - PROBABLY Drupal'],
		['/core/COPYRIGHT.txt', '   - PROBABLY Drupal'],
		['/modules/README.txt', '   - PROBABLY Drupal'],
		['/config.inc.php', '   - PROBABLY phpMyAdmin']
	]

	valid_status_codes = [200, 201, 202, 203, 204, 300, 301, 401, 403]
	try:
		for pair in path_pairs:
			req = requests.get("http://" + ip + pair[0])
			if (req.status_code) in valid_status_codes: 
				print(str(pair[0]) + str(pair[1]))
			else: 
				print('UNPREDICTABLE CMS')
	except:
		print ("problem connecting host")
		sys.exit(1)


print (estimate_cms(ip))
