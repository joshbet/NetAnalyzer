"""Tests for available updates on Windows 10 and 11.
Matthew Wells, 2021
"""

import win32com.client, platform
from pywintypes import com_error

class ConnectionError(BaseException):
    def __init__(self):
        super().__init__("Unable to connect to Windows Update Server.")

def check() -> (list, bool):
    """Uses the Windows Update Agent API to force a check for uninstalled
    Windows updates. Creates a list of updates containing keywords relating
    to security, and returns that list along with True if updates are missing
    and false if the computer is up-to-date.
    """
    app = win32com.client.Dispatch("Microsoft.Update.Session")
    searcher = app.CreateUpdateSearcher()
    try:
        uninstalled = searcher.Search("IsInstalled=0 and Type='Software'")
    except com_error:
        raise ConnectionError
    missing = [str(update) for update in uninstalled.Updates]
    keywords = [
        'security', 'malware', 'antivirus', 'defender', 'malicious',
        'firewall', 'antivirus', 'critical'
        ]
    critical_updates = []
    for update in missing:
        for keyword in keywords:
            if keyword in update.lower():
                critical_updates.append(update)
                break
    return critical_updates, missing != []

def format_update_check() -> dict:
    """Runs a check on the update status of the current machine, then creates
    a dictionary of potential issues and solutions. Returns problems and
    solutions in dictionary format, where issues are keys and solutions are
    values.
    """
    output = {}
    try:
        security_updates, result = check()
        if result:
            advice = "Visit the Settings menu and click on Windows Update."
            output["Your Windows machine is not up-to-date."] = advice
            warning = "Update your Windows machine immediately!"
            for update in security_updates:
                output["Security update " + update + " is missing."] = warning
    except ConnectionError as e:
        output[e.args[0]] = "Ensure your device is connected to the Internet."
    return output
