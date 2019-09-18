#!/usr/bin/env python3
import sys
import os
import subprocess
from host import start_host
from run_command import run_command

def main():
    url = sys.argv[1]   #first argument is going to be url
    ip = start_host(url)    #uses start_host functioni
    print(ip)
    path = os.getcwd()  #defines path as current working directory
    project_dir = path + '/RobustRecon'
    try:
        os.mkdir(project_dir)
        print('RobustRecon directory created.')
    except:
        print('RobustRecon directory already exists')

if __name__ == '__main__':
    main()

