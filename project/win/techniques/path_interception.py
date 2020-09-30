from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation


def print_path_interception_message():
    text = "( Path Interception Message )"
    print_title_technique(text)


def mitigation_audit():
    text = ("Find and eliminate path interception weaknesses in program "
    "configuration files, scripts, the PATH environment variable, services, "
    "and in shortcuts by surrounding PATH variables with quotation marks "
    "when functions allow for them. Be aware of the search order Windows "
    "uses for executing or loading binaries and use fully qualified paths "
    "wherever appropriate.\nClean up old Windows Registry keys when software "
    "is uninstalled to avoid keys with no associated legitimate binaries. "
    "Periodically search for and correct or report path interception "
    "weaknesses on systems that may have been introduced using custom or "
    "available tools that report software using insecure path configurations.")
    print_mitigation(text)


def mitigation_execution_prevention():
    text = ("Adversaries will likely need to place new binaries in locations "
    "to be executed through this weakness. Identify and block potentially "
    "malicious software executed path interception by using application "
    "whitelisting tools, like Windows Defender Application Control, AppLocker, "
    "or Software Restriction Policies where appropriate.")
    print_mitigation(text)


def mitigation_restrict_file_directory():
    text = "Require that all executables be placed in write-protected directories."
    print_mitigation(text)


def mitigation_user_account_management():
    text = ("Ensure that proper permissions and directory access control are set "
    "to deny users the ability to write files to the top-level directory C: and "
    "system directories, such as C:\Windows\, to reduce places where malicious "
    "files could be placed for execution.")
    print_mitigation(text)


def analyze():
    print_path_interception_message()
    mitigation_audit()
    mitigation_execution_prevention()
    mitigation_restrict_file_directory()
    mitigation_user_account_management()