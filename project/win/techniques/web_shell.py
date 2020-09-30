from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation


def print_web_shell():
    text = "( Web Shell )"
    print_title_technique(text)



def mitigation_privileged_account_manag():
    text = ("Audit account and group permissions to ensure that accounts "
    "used to manage servers do not overlap with accounts and permissions "
    "of users in the internal network that could be acquired through "
    "Credential Access and used to log into the Web server and plant a Web "
    "shell or pivot from the Web server into the internal network.")
    print_mitigation(text)


def mitigation_update_software():
    text = ("Ensure that externally facing Web servers are patched regularly "
    "to prevent adversary access through Exploitation for Privilege "
    "Escalation to gain remote code access or through file inclusion "
    "weaknesses that may allow adversaries to upload files or scripts that "
    "are automatically served as Web pages.")
    print_mitigation(text)


def analyze():
    print_web_shell()
    mitigation_privileged_account_manag()
    mitigation_update_software()