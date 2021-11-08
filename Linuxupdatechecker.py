#Script for checking firewall status on Linux

import sys
import os
import subprocess as sp

print('Admin password required to check for updates.')
#Gets root password from user
os.system('su')

#Performs upgrade command which lists software and system updates availible.
os.system('sudo apt-get upgrade')
print('   ')
print('System updates complete!')



		

