from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation


def print_parent_pid_spoofing_message():
    text = "( Parent PID Spoofing )"
    print_title_technique(text)


def mitigation_parent_pid_spoofing():
    text = ("This type of attack technique cannot be easily mitigated with "
    "preventive controls since it is based on the abuse of system features.")
    print_mitigation(text)


def analyze():
    print_parent_pid_spoofing_message()
    mitigation_parent_pid_spoofing()