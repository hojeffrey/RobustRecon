#!/usr/bin/env python3
import sys
import subprocess
from run_command import run_command

def start_host(url):
    print('Starting "host" to find IP Address...')
    command = 'host ' + url
    results = run_command(command)
    print('host complete~')
    return results

'''
def main():
    ip = sys.argv[1]
    host = start_host
    print(host(ip))

if __name__ == '__main__':
    main()
'''
