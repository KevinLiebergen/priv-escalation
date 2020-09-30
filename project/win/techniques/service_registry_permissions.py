from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation


def print_service_registry_message():
    text = "( Service Registry Permissions Weakness)"
    print_title_technique(text)


def mitigation_restrict_registry_permissions():
    text = ("Ensure proper permissions are set for Registry hives to prevent "
    "users from modifying keys for system components that may lead to "
    "privilege escalation.")
    print_mitigation(text)


def analyze():
    print_service_registry_message()
    mitigation_restrict_registry_permissions()