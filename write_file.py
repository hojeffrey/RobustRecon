#!/usr/bin/env python3
import sys

def write_file(path, data):
    f = open(path, 'w') #open file
    print(type(data))
    print(data)
    f.write(str(data))   #write data to the file
    f.close()   #close file


