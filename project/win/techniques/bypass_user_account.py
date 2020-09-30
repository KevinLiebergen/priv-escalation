from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation


def print_bypass_user_account_message():
    text = "( Bypass USer Account Control )"
    print_title_technique(text)


def mitigation_audit():
    text = ("Check for common UAC bypass weaknesses on Windows systems to be "
    "aware of the risk posture and address issues where appropriate.")
    print_mitigation(text)


def mitigation_privileged_account_manag():
    text = "Remove users from the local administrator group on systems."
    print_mitigation(text)


def mitigation_user_account_control():
    text = ("Although UAC bypass techniques exist, it is still prudent to use "
    "the highest enforcement level for UAC when possible and mitigate bypass "
    "opportunities that exist with techniques such as DLL Search Order Hijacking.")
    print_mitigation(text)

def analyze():
    print_bypass_user_account_message()
    mitigation_audit()
    mitigation_privileged_account_manag