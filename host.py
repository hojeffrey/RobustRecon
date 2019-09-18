#!/usr/bin/env python3
import sys
import subprocess
import run_command

def run_command(cmd):
    #this is corey's code to run a command and return result
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    #this needs edited so that the output splits at line rather than spitting it all out in one string
    output, error = process.communicate()
    return output

def start_host(ip):
    print('Performing DNS lookup with host...')
    command = 'host ' + ip
    results = run_command(command)
    print('DNS lookup complete~')
    return results

def main():
    ip = sys.argv[1]
    host = start_host
    print(host(ip))

if __name__ == '__main__':
    main()
