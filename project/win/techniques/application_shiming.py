from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation


def print_application_shiming_message():
    text = "( Application Shiming )"
    print_title_technique(text)


def mitigation_update_software():
    text = ("Microsoft released an optional patch update - KB3045645 - that "
    "will remove the 'auto-elevate' flag within the sdbinst.exe. This will "
    "prevent use of application shimming to bypass UAC.")
    print_mitigation(text)


def mitigation_user_accont_control():
    text = ("Changing UAC settings to 'Always Notify' will give the user more "
    "visibility when UAC elevation is requested, however, this option will not "
    "be popular among users due to the constant UAC interruptions.")
    print_mitigation(text)


def analyze():
    print_application_shiming_message()
    mitigation_update_software()
    mitigation_user_accont_control()