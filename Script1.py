#!/usr/bin/python3
#NetAnalyzer Script


import socket
import nmap

#Commonly used ports
begin = 20
end = 445

#Gets hostname and local IP
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

nmScan = nmap.PortScanner()

#print(hostname)
print(local_ip)
print("      ")
print("      ")

#Loop that will check each port from the begin to end variable
for i in range(begin,end+1):
    
    result = nmScan.scan(local_ip,str(i))
    
    
    state = result['scan'][local_ip]['tcp'][i]['state']
    
    if state == "open":
        print(f'port {i} is {result}')



