#!/usr/bin/env python3
import sys

from host import start_host
# from cms import estimate_cms
# from nmap-waf import start_nmap

def main():
    url = sys.argv[1]
    ##Given a host derive an IP address.
    ip = start_host(url)
    # cms_type = estimate_cms(ip)
    # print('Estimated CMS Type: ' + cms_type)

    # nmap_results = start_nmap(ip, options)
    # write_file(file_name, nmap_results)
    # print('Results have been written ' + file_name)

    # ip = sys.argv[1]
    

if __name__ == '__main__':
    main()
