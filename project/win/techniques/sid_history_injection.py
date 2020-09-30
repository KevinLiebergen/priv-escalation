from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation


def print_sid_history_message():
    text = "( SID History Injection )"
    print_title_technique(text)


def mitigation_active_directory_config():
    text = ("Clean up SID-History attributes after legitimate account "
    "migration is complete.\nConsider applying SID Filtering to "
    "interforest trusts, such as forest trusts and external trusts, "
    "to exclude SID-History from requests to access domain resources. "
    "SID Filtering ensures that any authentication requests over a trust "
    "only contain SIDs of security principals from the trusted domain (i.e "
    "preventing the trusted domain from claiming a user has membership in "
    "groups outside of the domain).\n\nSID Filtering of forest trusts is "
    "enabled by default, but may have been disabled in some cases to allow "
    "a child domain to transitively access forest trusts. SID Filtering of "
    "external trusts is automatically enabled on all created external trusts "
    "using Server 2003 or later domain controllers. However note that SID "
    "Filtering is not automatically applied to legacy trusts or may have been "
    "deliberately disabled to allow inter-domain access to resources.\nSID "
    "Filtering can be applied by:\n\n- Disabling SIDHistory on forest trusts "
    "using the netdom tool (netdom trust /domain: /EnableSIDHistory:no on "
    "the domain controller)\n- Applying SID Filter Quarantining to external "
    "trusts using the netdom tool (netdom trust /domain: /quarantine:yes "
    "on the domain controller)\n- Applying SID Filtering to domain trusts "
    "within a single forest is not recommended as it is an unsupported "
    "configuration and can cause breaking changes. If a domain within a "
    "forest is untrustworthy then it should not be a member of the forest. "
    "In this situation it is necessary to first split the trusted and "
    "untrusted domains into separate forests where SID Filtering can be "
    "applied to an interforest trust.")
    print_mitigation(text)

def analyze():
    print_sid_history_message()
    mitigation_active_directory_config()