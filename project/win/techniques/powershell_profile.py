from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation


def print_powershell_profile_message():
    text = "( PowerShell Profile )"
    print_title_technique(text)


def mitigation_code_signing():
    text = ("Enforce execution of only signed PowerShell scripts. "
    "Sign profiles to avoid them from being modified.")
    print_mitigation(text)


def mitigation_restrict_files_directory():
    text = ("Making PowerShell profiles immutable and only changeable "
    "by certain administrators will limit the ability for adversaries "
    "to easily create user level persistence.")
    print_mitigation(text)


def mitigation_software_configuration():
    text = ("Avoid PowerShell profiles if not needed. Use the -No Profile "
    "flag with when executing PowerShell scripts remotely to prevent local "
    "profiles and scripts from being executed.")
    print_mitigation(text)


def analyze():
    print_powershell_profile_message()
    mitigation_code_signing()
    mitigation_restrict_files_directory()
    mitigation_software_configuration()