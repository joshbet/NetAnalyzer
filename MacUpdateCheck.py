#!/usr/bin/python3
#Script for checking for software updates on MacOS and checking the current OS version

import sys
import os
import subprocess as sp

updatesoftware = ("softwareupdate -l")
verscheck = ("sw_vers")


print("Checking for software updates...")
print(os.system(updatesoftware))
print("Done!")



print(os.system(verscheck))

        