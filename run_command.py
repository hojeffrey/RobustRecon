#!/usr/bin/env python3
import sys
import subprocess

def run_command(cmd):
    #this is corey's code to run a command and return result
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    #this needs edited so that the output splits at line rather than spitting it all out in one string
    output, error = process.communicate()
    return output
