#!/usr/bin/python3
#NetAnalyzer Script


import socket
import nmap

def main(ip=None):
    #Commonly used ports
    begin = 20
    end = 445

    #Gets hostname and local IP
    hostname = socket.gethostname()
    if not (ip):
        ip = socket.gethostbyname(hostname)

    nmScan = nmap.PortScanner()

##    #print(hostname)
##    print(local_ip)
##    print("      ")
##    print("      ")

    result = nmScan.scan(ip, str(begin) + '-' + str(end)) #By moving our scan out of the loop and using the built in range scan, we increase speed several hundredfold -Matthew
    keys = nmScan[ip]['tcp'].keys() #We only care about ports that are actually open, so we'll make a list of them here - Matthew
    output = [] #Hold output in a list of strings so the interface can display them -Matthew
  
    #Loop that will check each port from the begin to end variable
    for i in keys:
        
        state = result['scan'][ip]['tcp'][i]['state']
        
        if state == "open":
##            print(f'port {i} is {result}')
            output.append(f'port {i} is {state}')

    return output



