#!/usr/bin/python3


import platform

os = platform.platform()

print(os)

if 'mac' in os:
    print('This system is running macOS')

if 'windows' in os:
    print('This system is running Windows')

if 'linux' in os:
    print('This system is running Linux')
