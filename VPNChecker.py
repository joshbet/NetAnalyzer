"""This script provides a wrapper on OS-specific VPN analysis. Currently
supports Windows 10/11.
Matthew Wells, 2021
"""

import subprocess, platform

def windows_vpn_check() -> (dict, bool):
    """Uses subprocess in order to make a call to Windows PowerShell and get
    VPN connection data, then parses the return data to get all current VPNs'
    configuration. Returns a dict with the data of all saved VPNs, and a bool
    that is true if connected to a VPN and false otherwise.
    """
    return_val = subprocess.run(
        ["powershell", "-Command", "Get-VpnConnection"],
        capture_output=True
        )
    text = return_val.stdout.decode('UTF-8')
    text = text.split('\r\n')
    while '' in text:
        text.remove('')
    vpn_config = {}
    connected = False
    while text != []:
        connection = text[:15]
        text = text[15:]
        name = connection[0].split(':')[1].strip(' ')
        vpn_config[name] = {}
        for line in connection:
            key, value = line.split(':')
            key = key.strip(' ')
            value = value.strip(' ')
            vpn_config[name][key] = value
            if key == 'ConnectionStatus' and value == 'Connected':
                connected = True
    return vpn_config, connected

def format_vpn_check() -> dict:
    """Runs a check on the saved VPN configurations of the current machine, then
    creates a dictionary of potential issues and solutions. Returns problems and
    solutions in dictionary format, where issues are keys and solutions are
    values.
    """
    output = {}
    os = platform.platform()
    if 'windows' in os.lower():
        vpn_configs, status = windows_vpn_check()
    else:
        vpn_configs = {}
        status = False
    if not status:
        if vpn_configs == {}:
            problem = 'No Virtual Private Network configuration detected.'
            solution = 'Add a VPN configuration to this device.'
        else:
            problem = 'You are not using any of your VPNs.'
            solution = 'Make sure your VPN configurations are up-to-date'
            solution += ' and currently enabled.'
        output[problem] = solution
    return output
