from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation


def print_new_service_message():
    text = "( New Service )"
    print_title_technique(text)


def mitigation_user_Accout_manag():
    text = ("Limit privileges of user accounts and remediate Privilege "
    "Escalation vectors so only authorized administrators can create new services.")
    print_mitigation(text)


def analyze():
    print_new_service_message()
    mitigation_user_Accout_manag()