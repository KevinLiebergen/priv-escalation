from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation


def print_appcert_dlls():
    text = "( AppCert DLLs )"
    print_title_technique(text)


def mitigation_execution_prevention():
    text = ("Adversaries install new AppCertDLL binaries to execute this technique. "
    "Identify and block potentially malicious software executed through "
    "AppCertDLLs functionality by using application whitelisting tools, "
    "like Windows Defender Application Control, AppLocker, or Software "
    "Restriction Policies where appropriate.")
    print_mitigation(text)


def analyze():
    print_appcert_dlls()
    mitigation_execution_prevention()