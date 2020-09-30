from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation


def print_valid_accounts():
    text = "( Searching Valid Accounts )"
    print_title_technique(text)


def mitigation_app_developer_guidance():
    text = ("Ensure that applications do not store sensitive data or "
    "credentials insecurely. (e.g. plaintext credentials in code, published "
    "credentials in repositories, or credentials in public cloud storage).")
    print_mitigation(text)


def mitigation_audit():
    text = ("Routinely audit source code, application configuration files, "
    "open repositories, and public cloud storage for insecure use and storage "
    "of credentials.")
    print_mitigation(text)


def mitigation_filter_network_traffic():
    text = ("Cloud service providers support IP-based restrictions when "
    "accessing cloud resources. Consider using IP whitelisting on cloud-based "
    "systems along with user account management to ensure that data access "
    "is restricted not only to valid users but only from expected IP ranges "
    "to mitigate the use of stolen credentials to access data.")
    print_mitigation(text)


def mitigation_multifactor_authentication():
    text = ("Integrating multi-factor authentication (MFA) as part of "
    "organizational policy can greatly reduce the risk of an adversary gaining "
    "control of valid credentials that may be used for additional tactics "
    "such as initial access, lateral movement, and collecting information. "
    "MFA can also be used to restrict access to cloud resources and APIs.")
    print_mitigation(text)


def mitigation_password_policies():
    text = ("Applications and appliances that utilize default username and "
    "password should be changed immediately after the installation, and "
    "before deployment to a production environment. When possible, "
    "applications that use SSH keys should be updated periodically and "
    "properly secured. Ensure that local administrator accounts have complex, "
    "unique passwords across all systems on the network.\nIn cloud "
    "environments, consider rotating access keys within a certain number of "
    "days for reducing the effectiveness of stolen credentials.")
    print_mitigation(text)


def mitigation_privileged_account_manag():
    text = ("Audit domain and local accounts as well as their permission "
    "levels routinely to look for situations that could allow an adversary to "
    "gain wide access by obtaining credentials of a privileged account. These "
    "audits should also include if default accounts have been enabled, or if "
    "new local accounts are created that have not be authorized. Do not put "
    "user or admin domain accounts in the local administrator groups across "
    "systems unless they are tightly controlled and use of accounts is "
    "segmented, as this is often equivalent to having a local administrator "
    "account with the same password on all systems. Follow best practices "
    "for design and administration of an enterprise network to limit "
    "privileged account use across administrative tiers. Limit credential "
    "overlap across systems to prevent access if account credentials are obtained.")
    print_mitigation(text)


def mitigation_user_account_manag():
    text = ("Ensure users and user groups have appropriate permissions for their "
    "roles through Identity and Access Management (IAM) controls. Configure user "
    "permissions, groups, and roles for access to cloud-based systems as well. "
    "Implement strict IAM controls to prevent access to systems except for the "
    "applications, users, and services that require access. Consider using "
    "temporary credentials that are only good for a certain period of time "
    "in cloud environments to reduce the effectiveness of compromised accounts.")
    print_mitigation(text)


def analyze():
    print_valid_accounts()
    mitigation_app_developer_guidance()
    mitigation_audit()
    mitigation_filter_network_traffic()
    mitigation_multifactor_authentication()
    mitigation_password_policies()
    mitigation_privileged_account_manag()
    mitigation_user_account_manag()