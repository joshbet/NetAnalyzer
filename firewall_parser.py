"""Gets current firewall state and parses it into a dict. Requires netsh, and
thus runs on Windows 2000 and later.
Matthew Wells, 2021
"""

import subprocess

def firewall_check() -> dict[dict]:
    """Returns a dictionary containing Domain, Private, and Public
    sub-dictionaries. Each sub-dictionary contains the current state of the
    firewall for its respective scope. Uses netsh to get the state as binary
    data.
    """
    firewall_output = {"Domain":{}, "Private":{}, "Public":{}}
    try:
        text = str(
            subprocess.check_output('netsh advfirewall show allprofiles')
            )
    except:
        print("FileNotFoundError: netsh is unavailable.")
        firewall_output["Domain"]["Status"] = ["Firewall data unavailable."]
        firewall_output["Private"]["Status"] = ["Firewall data unavailable."]
        firewall_output["Public"]["Status"] = ["Firewall data unavailable."]
        return firewall_output
    text = text.split('\\r\\n')
    domain_text_params = text[3:10] + text[12:16]
    private_text_params = text[20:27] + text[29:33]
    public_text_params = text[37:44] + text[46:50]
    for line in domain_text_params:
        key = line.split('  ')[0]
        value = line.split('  ')[-1].strip(' ')
        firewall_output["Domain"][key] = value
    for line in private_text_params:
        key = line.split('  ')[0]
        value = line.split('  ')[-1].strip(' ')
        firewall_output["Private"][key] = value
    for line in public_text_params:
        key = line.split('  ')[0]
        value = line.split('  ')[-1].strip(' ')
        firewall_output["Public"][key] = value
    return firewall_output
    
    
