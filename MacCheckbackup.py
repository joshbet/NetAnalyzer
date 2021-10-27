#!/usr/bin/python3
#Script for checking backup status on macOS

import sys
import os
import subprocess as sp

print("Backups on macOS are handled through the TimeMachine utility, this script will display the current status of backups.")

checkbackup = sp.getoutput('tmutil listbackups')
enablebackup = ('sudo tmutil enable')

if checkbackup == 'No machine directory found for host.':
    print("Backup not enabled")
    print("    ")
    uinput = input("Would you like to enable TimeMachine backup? Enter Y or N.")
    if uinput == "Y":
        os.system(enablebackup)
        print("Backup now enabled")
    if uinput == "N":
        print("Exiting...")
        exit 

