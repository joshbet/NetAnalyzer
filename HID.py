#!/usr/bin/python3

import sys
import usb.core


flag = 0
index = 0
usbidsfile = open("usb.ids","r", encoding="utf-8")

readfile = usbidsfile.read()

# find USB devices
dev = usb.core.find(find_all=True)
# loop through devices, printing vendor and product ids in decimal and hex
for cfg in dev:
    vendid = hex(cfg.idVendor)
    productid= hex(cfg.idProduct)
    print(vendid)
    print(productid)
    #print(cfg.idVendor)
    
    if vendid in readfile:
        print('yes')
    else:
        print('no')