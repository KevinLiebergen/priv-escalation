from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation


def print_file_system_permissions_message():
    text = "( Filesystem permissions )"
    print_title_technique(text)


def mitigation_audit():
    text = ("Use auditing tools capable of detecting file system permissions "
    "abuse opportunities on systems within an enterprise and correct them. "
    "Toolkits like the PowerSploit framework contain PowerUp modules that can "
    "be used to explore systems for service file system permissions weaknesses.")
    print_mitigation(text)


def mitigation_user_account_control():
    text = ("Turn off UAC's privilege elevation for standard users "
    "[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System] "
    "to automatically deny elevation requests, add: 'ConsentPromptBehaviorUser'"
    "=dword:00000000. Consider enabling installer detection for all users by "
    "adding: 'EnableInstallerDetection'=dword:00000001. This will prompt for "
    "a password for installation and also log the attempt. "
    "\nTo disable installer detection, instead add: 'EnableInstallerDetection'"
    "=dword:00000000. This may prevent potential elevation of privileges through "
    "exploitation during the process of UAC detecting the installer, but will "
    "allow the installation process to continue without being logged.")
    print_mitigation(text)


def mitigation_user_account_manag():
    text = ("Limit privileges of user accounts and groups so that only authorized "
    "administrators can interact with service changes and service binary target path "
    "locations. Deny execution from user directories such as file download directories "
    "and temp directories where able.")
    print_mitigation(text)


def analyze():
    print_file_system_permissions_message()
    mitigation_audit()
    mitigation_user_account_control()
    mitigation_user_account_manag()