#!/usr/bin/env python3
import sys
import os
import requests
import socket
import subprocess

def run_command(cmd):
    #this is corey's code to run a command and return result
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    #this needs edited so that the output splits at line rather than spitting it all out in one string
    output, error = process.communicate()
    return output

#def write_file(path, data):
#    f = open(path, 'w') #open file
#    print(type(data))
#    print(data)
#    f.write(str(data))   #write data to the file
#    f.close()   #close file
    
def start_nikto(options, ip):
    #ip = sys.argv[1]
    print('starting nikto')
    command = 'nikto ' + options + ' http://' + ip  #this is equivalent of  what you would usually type into bash command line
    results = run_command(command) #start a new process
    print('Nikto scan complete~')
#    print(results)
    return(results)

#ROOT_DIR = 'IP_Targets' #this is where we name our root directory
#create_dir(ROOT_DIR) #this creates root directory

#def create_report(input):
#    project_dir = ROOT_DIR + '/' + ip
#    create_dir(project_dir)

def main():
    ip = sys.argv[1]
#    if ip is not actually an ip, then lets assume its a url, then convert ip to url
    path = os.getcwd()
    project_dir = path + '/RobustRecon'
    try:
        os.mkdir(project_dir)
        print('RobustRecon directory created.')
    except:
        print('RobustRecon directory already exists')
    nikto = start_nikto('-h', ip)   #option will be -h and ip will be 1st argument on command line
    write_file(project_dir + '/nikto.txt', nikto)
    nmap = start_nmap(' -p80 --script http-waf-detect', ip)
    write_file(project_dir + '/nmap.txt', nmap)


if __name__ == '__main__':
    main()
