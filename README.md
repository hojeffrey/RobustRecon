# Fullstackcyber

![robust-recon-logo](https://github.com/hojeffrey/Fullstackcyber/blob/test-branch/robust-recon-logo.png)

 Robust Recon is a tool created to condense reconnaissance from hours to minutes. It can convert a url to an ip, detect a Web Application Firewall, bruteforce to determine directory paths, make an estimate on which CMS it is running, perform a vulnerability scan, and more. Best of all, it organizes your data in a neat directory. 


## Prerequisites: 
- Kali Linux
  - wafw00f
  - nikto 

## Installing:
Download the zip file. Move file to a folder of your choice. Unzip.
```
unzip robustrecon.zip
```
  
Replace `/path/to` with current location of the files and replace `/usr/local/bin` with a location of your choice
```
ln -s ./path/to/main.py /usr/local/bin/robustrecon
```

## To Run Robust Recon:
Go to the location you saved Robust Recon. Enter an ip or a url as the first argument. Enter a wordlist of your choice for the second argument.
```
robustrecon hackthissite.org wordlist
```

1st Argument = url OR ip

2nd Argument = wordlist of your choice

## To View Results:
The folder will be labelled with the IP Address of your target.
```
cd 'Robust Recon: 255.255.255.255'
```
`cat` each file to see the full printed results.
```
cat nikto.txt
```

## Authors

* **Jeffrey Ho** - *Initial work* - [hojeffrey](https://github.com/hojeffrey)
* **Sarah Gold** - *Initial work* - [g0ldleaf](https://github.com/g0ldleaf)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to the Fullstack Academy Cyber team for their guidance
* Thanks to the creators of nmap, nikto, and wafw00f
