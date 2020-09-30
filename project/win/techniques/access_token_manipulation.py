from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation


def print_access_token_manipulation():
    text = "( Access token manipulation )"
    print_title_technique(text)


def mitigation_user_account_management():
    text = ("An adversary must already have administrator level access on the "
    "local system to make full use of this technique; be sure to restrict users "
    "and accounts to the least privileges they require.")
    print_mitigation(text)


def mitigation_privileged_account_management():
    text = ("Limit permissions so that users and user groups cannot create tokens. "
    "This setting should be defined for the local system account only. GPO: Computer "
    "Configuration > [Policies] > Windows Settings > Security Settings > Local "
    "Policies > User Rights Assignment: Create a token object. Also define who can "
    "create a process level token to only the local and network service through GPO: "
    "Computer Configuration > [Policies] > Windows Settings > Security Settings "
    "> Local Policies > User Rights Assignment: Replace a process level token.")
    print_mitigation(text)


def analyze():
    print_access_token_manipulation()
    mitigation_user_account_management()
    mitigation_privileged_account_management()
