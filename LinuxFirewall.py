#Script for checking firewall status on Linux

import sys
import os
import subprocess as sp

#This command installs the prerequisite tool UFW (Uncomplicated Firewall)
os.system('sudo apt-get install ufw')


print('    ')

#Checks the status and saves it as a variable
status = sp.getoutput('sudo ufw status')

#If the firewall status is inactive it will ask if the user would like to enable it via command.
if status == 'Status: inactive':
	print('Firewall is disabled, would you like to enable it?')
	
	uinput = input('Enter Y/N')
	
	if uinput == 'y' or 'Y':
		print(os.system('sudo ufw enable'))
		print('Firewall now enabled!')
	else:
		print('Exiting...')
		sys.exit()
		

