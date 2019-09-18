#!/usr/bin/env python3
import sys
import subprocess
from run_command import run_command

def start_nikto(options, ip):
    print('Starting nikto...')
    command = 'nikto ' + options + ' http://' + ip  #this is equivalent of  what you would usually type into bash command line
    results = run_command(command) #start a new process
    print(results)
    print('Nikto scan complete~')
    return results

'''
def main():
    ip = sys.argv[1]
    nikto = start_nikto('-h', ip)
    print(type(nikto))

if __name__ == '__main__':
    main()
'''
