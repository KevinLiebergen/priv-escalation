from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation


def print_scheduled_task_message():
    text = "( Scheduled Task )"
    print_title_technique(text)


def mitigation_audit():
    text = ("Toolkits like the PowerSploit framework contain PowerUp modules "
    "that can be used to explore systems for permission weaknesses in "
    "scheduled tasks that could be used to escalate privileges.")
    print_mitigation(text)


def mitigation_operating_system_configuration():
    text = ("Configure settings for scheduled tasks to force tasks to run "
    "under the context of the authenticated account instead of allowing "
    "them to run as SYSTEM. The associated Registry key is located at "
    "HKLM\SYSTEM\CurrentControlSet\Control\Lsa\SubmitControl. The setting "
    "can be configured through GPO: Computer Configuration > [Policies] > "
    "Windows Settings > Security Settings > Local Policies > Security "
    "Options: Domain Controller: Allow server operators to schedule tasks, "
    "set to disabled.")
    print_mitigation(text)


def mitigation_privileged_account_manag():
    text = ("Configure the Increase Scheduling Priority option to only allow "
    "the Administrators group the rights to schedule a priority process. "
    "This can be can be configured through GPO: Computer Configuration > "
    "[Policies] > Windows Settings > Security Settings > Local Policies > "
    "User Rights Assignment: Increase scheduling priority.")
    print_mitigation(text)


def mitigation_user_account_manag():
    text = ("Limit privileges of user accounts and remediate Privilege "
    "Escalation vectors so only authorized administrators can create "
    "scheduled tasks on remote systems.")
    print_mitigation(text)


def analyze():
    print_scheduled_task_message()
    mitigation_audit()
    mitigation_operating_system_configuration()
    mitigation_privileged_account_manag()
    mitigation_user_account_manag()