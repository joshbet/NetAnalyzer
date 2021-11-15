#Script for checking when the password was last changed in Linux
#passwordcheck.sh is required for script to work properly.


import sys
import os
import subprocess as sp

passwordsh = 'bash passwordcheck.sh'

#os.system(passwordsh)
systemdate = sp.getoutput('date +"%y-%m-%d"')
modifydate = sp.getoutput(passwordsh)

date = modifydate.replace('Modify: ','')
date = date.replace('-0500','')
passwdtxt = 'The password on for this system was last changed on'

print(passwdtxt,date)
print(" ")

