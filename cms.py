#!/usr/bin/python3

import requests 
import sys

def estimate_cms(ip):
	path_pairs = [
		['/wp-login/', 'WORDPRESS'], 
		['/wp-admin/', 'WORDPRESS'], 
		['/readme.html','WORDPRESS'],
		['/wp-config', 'WORDPRESS'],
		['/administrator/', 'Joomla'],
		['/readme.txt', 'Joomla'],
		['/media/com_joomlaupdate/', 'Joomla'],
		['index.php/admin/', 'Magento'],
		['/RELEASE_NOTES.txt', 'Magento'],
		['/js/mage/cookies.js', 'Magento'],
		['index.php', 'Magento'],
		['/skin/frontend/default/default/css/styles.css', 'Magento'],
		['/skin/frontend/default/default/css/styles.css', 'Magento'],
		['/errors/design.xml', 'Magento'],
		['/readme.txt', 'Drupal'],
		['/core/COPYRIGHT.txt', 'Drupal'],
		['/modules/README.txt', 'Drupal'],
		['/config.inc.php', 'phpMyAdmin']
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


