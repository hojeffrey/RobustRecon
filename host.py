#!/usr/bin/env python3
import sys
import subprocess
from run_command import run_command

def start_host(url):
#    print('Starting "host" to find IP Address...')
#    command = 'host ' + url + ' | head -1 | cut -d\' \' -f4'
    command = 'host ' + url
    #host scanme.nmap.org | head -1 | cut -d' ' -f4 (in bash)
    print(command)
    results = run_command(command).decode('utf-8')  #utf-8 changes bytes to string
    start_location = results.index('has address') + 12  #represents where the string starts so its not static
    stop_location = results.index('\n')
    ip = results[start_location:stop_location]
#    print(ip)
    #print('host complete~')
#    print(results)
    return(ip) 

'''
def main():
    url = sys.argv[1]
    host = start_host(url)
    print(host)

if __name__ == '__main__':
    main()
'''
