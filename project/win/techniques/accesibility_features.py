from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation


def print_accesibility_fatures_message():
    text = "( Accesibility features )"
    print_title_technique(text)


def mitigation_execution_prevention():
    text = ("Adversaries can replace accessibility features binaries with "
    "alternate binaries to execute this technique. Identify and block "
    "potentially malicious software executed through accessibility features "
    "functionality by using application whitelisting tools, like Windows "
    "Defender Application Control, AppLocker, or Software Restriction Policies "
    "where appropriate.")
    print_mitigation(text)


def mitigation_limit_access_network():
    text = ("If possible, use a Remote Desktop Gateway to manage connections "
    "and security configuration of RDP within a network.")
    print_mitigation(text)


def mitigation_operating_system_config():
    text = ("To use this technique remotely, an adversary must use it in "
    "conjunction with RDP. Ensure that Network Level Authentication is enabled "
    "to force the remote desktop session to authenticate before the session is "
    "created and the login screen displayed. It is enabled by default on "
    "Windows Vista and later.")
    print_mitigation(text)


def analyze():
    print_accesibility_fatures_message()
    mitigation_execution_prevention()
    mitigation_limit_access_network()
    mitigation_operating_system_config()