#!/usr/bin/python3
#Script for checking firewall status on macOS

import sys
import os
import subprocess as sp

#Gets output of firewall status as either a 1 or 0
output = sp.getoutput('defaults read /Library/Preferences/com.apple.alf globalstate')

#Command used to enable firewall
enablefirewall = ('sudo defaults write /Library/Preferences/com.apple.alf globalstate -int 1')

#print(enablefirewall)
#print(output)

if output == '1':
    print('Firewall is Enabled')

if output == '0':
    print('Firewall is Disabled')
    print('         ')
    #Asks for user input to make a decision whether or not to enable the firewall on the system
    uinput = input("Would you like to enable the firewall? Enter Y or N.")
    
    if uinput == 'y' or 'Y':
        os.system(enablefirewall)
        print('Firewall is now enabled.')
        sys.exit()
    else:
        print('Exiting...')
        sys.exit()
        
        