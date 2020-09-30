from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation


def print_appinit_dlls():
    text = "( AppInit DLLs )"
    print_title_technique(text)


def mitigation_execution_prevention():
    text = ("Adversaries can install new AppInit_DLLs binaries to execute this "
    "technique. Identify and block potentially malicious software executed "
    "through AppInit_DLLs functionality by using application whitelisting tools, "
    "like Windows Defender Application Control, AppLocker, or Software Restriction "
    "Policies where appropriate.")
    print_mitigation(text)


def mitigation_update_software():
    text = "Upgrade to Windows 8 or later and enable secure boot."
    print_mitigation(text)


def analyze():
    print_appinit_dlls()
    mitigation_execution_prevention()
    mitigation_update_software()