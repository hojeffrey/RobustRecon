#!/usr/bin/env python3
import sys
import os
import subprocess
import requests
from host import start_host
from run_command import run_command
from nikto import start_nikto
from write_file import write_file
from waf_detect import start_wafw00f
#from colorama import Fore, Style    #for cms
from cms import estimate_cms
from directorybruteforce import bruteforce

def main():
    url = sys.argv[1]   #first argument is going to be url
    ip = start_host(url)    #uses start_host functioni
    wordlist = sys.argv [2]
    print('IP Address found:' + ip)
    path = os.getcwd()  #defines path as current working directory
    project_dir = path + '/RobustRecon: ' + ip
    try:
        os.mkdir(project_dir)
        print('RobustRecon directory created.')
    except:
        print('RobustRecon directory already exists')
    print("[+] Starting Web Application Firewall using wafw00f...")
    waf_detect = start_wafw00f(ip)
    write_file(project_dir + '/waf_detect.txt', waf_detect)
    print('waf_detect.txt created')
    print("[+] Starting to get a Estimate on the CMS...")
    cms = (estimate_cms(ip))
    write_file(project_dir + '/cms.txt', cms)
    print('cms.txt created')
    print("[+] Starting to bruteforce directory paths...")
    brute = (bruteforce(ip, wordlist))
    write_file(project_dir + '/directorybruteforce.txt', brute)
    print('directorybruteforce.txt created')
    print("[+] Starting to run a nikto scan")
    nikto = start_nikto(url)
    write_file(project_dir + '/nikto.txt', nikto) 
    print('nikto.txt created') 
if __name__ == '__main__':
    main()

