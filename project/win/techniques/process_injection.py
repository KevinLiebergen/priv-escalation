from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation


def print_process_injection_message():
    text = "( Process Injection Message )"
    print_title_technique(text)


def mitigation_behavior_prevention():
    text = ("Some endpoint security solutions can be configured to block "
    "some types of process injection based on common sequences of behavior "
    "that occur during the injection process.")
    print_mitigation(text)


def analyze():
    print_process_injection_message()
    mitigation_behavior_prevention()