#Script for checking processes on Linux

import sys
import os
import subprocess as sp

print('Checking running processes...')
		
os.system('ps aux')

print('Check above for any unknown processes that are running.')
