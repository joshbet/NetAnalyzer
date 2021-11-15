#Script for checking VPN status on Linux
#checkvpn.sh is required for this script to work properly.

import sys
import os
import subprocess as sp

vpnsh = 'bash checkvpn.sh'

#Runs script that checks VPN status
os.system(vpnsh)

status = sp.getoutput(vpnsh)

if status == 'VPN down':
	print('VPN Is down, Would you like to learn how to set up a VPN?')
	uinput = input('Enter Y/N')
	
	if uinput == 'y' or 'Y':
		print('The link below has different types of VPNs that are compatible with this system:')
		print('https://wiki.ubuntu.com/VPN')
		sys.exit()
	else:
		print('Exiting...')
		sys.exit()
if status == 'VPN up':
	print('VPN is enabled.')
	sys.exit()
	


