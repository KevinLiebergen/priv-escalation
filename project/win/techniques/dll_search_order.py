from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation


def print_dll_search_order_message():
    text = "( DLL Search Order Hijacking )"
    print_title_technique(text)


def mitigation_audit():
    text = ("Use auditing tools capable of detecting DLL search order "
    "hijacking opportunities on systems within an enterprise and correct "
    "them. Toolkits like the PowerSploit framework contain PowerUp modules "
    "that can be used to explore systems for DLL hijacking weaknesses.")
    print_mitigation(text)


def mitigation_execution_prevention():
    text = ("Adversaries may use new DLLs to execute this technique. "
    "Identify and block potentially malicious software executed through "
    "search order hijacking by using application whitelisting solutions "
    "capable of blocking DLLs loaded by legitimate software.")
    print_mitigation(text)


def mitigation_restrict_library_loading():
    text = ("Disallow loading of remote DLLs. This is included by default "
    "in Windows Server 2012+ and is available by patch for XP+ and Server 2003+. "
    "Path Algorithm Enable Safe DLL Search Mode to force search for system DLLs "
    "in directories with greater restrictions (e.g. %SYSTEMROOT%)to be used before "
    "local directory DLLs (e.g. a user's home directory). The Safe DLL Search Mode "
    "can be enabled via Group Policy at Computer Configuration > [Policies] > Administrative "
    "Templates > MSS (Legacy): MSS: (SafeDllSearchMode) Enable Safe DLL search mode.\n" 
    "The associated Windows Registry key for this is located at "
    "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\SafeDLLSearchMode.")
    print_mitigation(text)


def analyze():
    print_dll_search_order_message()
    mitigation_audit()
    mitigation_execution_prevention()
    mitigation_restrict_library_loading()