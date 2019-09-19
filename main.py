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
from colorama import Fore, Style    #for cms
from cms import estimate_cms

def main():
    url = sys.argv[1]   #first argument is going to be url
    ip = start_host(url)    #uses start_host functioni
    print('IP Address found:' + ip)
    path = os.getcwd()  #defines path as current working directory
    project_dir = path + '/RobustRecon: ' + ip
    try:
        os.mkdir(project_dir)
        print('RobustRecon directory created.')
    except:
        print('RobustRecon directory already exists')
    waf_detect = start_wafw00f(ip)
    write_file(project_dir + '/waf_detect.txt', waf_detect)
    print('waf_detect.txt created')
    cms = (estimate_cms(ip))
    write_file(project_dir + '/cms.txt', cms)
    print('cms.txt created')
    nikto = start_nikto(url)
    write_file(project_dir + '/nikto.txt', nikto)
    print('nikto.txt created')

if __name__ == '__main__':
    main()

