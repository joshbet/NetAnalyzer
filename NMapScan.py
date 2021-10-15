#!/usr/bin/python3
#NetAnalyzer Script


import socket
import nmap

def main(ip=None) -> list[str]:
    """This function checks for data on open ports with nmap. It returns
    a list of strings describing the states of each port. If a string
    containing an IP to search is provided, it uses that IP to check ports.
    If no IP is provided, it returns ports on the device it is running on.
    """
    #Commonly used ports
    begin = 20
    end = 445

    #Gets hostname and local IP
    hostname = socket.gethostname()
    if not (ip):
        ip = socket.gethostbyname(hostname)

    nmScan = nmap.PortScanner()

    result = nmScan.scan(ip, str(begin) + '-' + str(end)) 
    keys = nmScan[ip]['tcp'].keys()
    vulnerabilities = []
    solutions = {}
  
    #Loop that will check each port from the begin to end variable
    for i in keys:
        
        state = result['scan'][ip]['tcp'][i]['state']
        
        if state == "open":
            problem = f'port {i} is {state}'
            vulnerabilities.append(problem)
            solutions[problem] = f'Secure port {i}'

    return vulnerabilities, solutions



