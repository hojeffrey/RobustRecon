#!/usr/bin/env python3
import sys
import subprocess
from run_command import run_command
'''
def start_nikto(url):
    print('Starting nikto...')
    command = 'nikto -h ' + url  #this is equivalent of  what you would usually type into bash command line
    results = run_command(command) #start a new process
    print(results)
    print('Nikto scan complete~')
    return results
'''
def start_nikto(url):
    command = ['nikto', '-h', url]
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True)   #executes command on os level
    results = ''
    print('Starting nikto scan...')
    print('Check nikto.txt. Scan may take a few minutes.')
    while True:
        output = proc.stdout.readline() #read output of the process line by line
#        print(output.strip())   #print output to screen
        results += output   #add output to a returnable string
        exit_code = proc.poll() #check to see if the process had finished
        if exit_code is not None:   #exit code is set when the process is finished. 'none' exit code means process is still running.
#            print('RETURN_CODE', exit_code) #print exit code to proove that process finished
            break   #quit the while loop
    return(results)
'''
def main():
    url = sys.argv[1]
    nikto = start_nikto(url)

if __name__ == '__main__':
    main()
'''
