#!/usr/bin/python3

from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation

import subprocess

def print_process_injection():
	text = "( Process Injection )"
	print_title_technique(text)


def check_protecion_ptrace():
	print(open_green + "\nSearching reading permissions for syscalls tracer (ptrace, strace, etc)\n" + close)
	out = subprocess.Popen(['cat', '/proc/sys/kernel/yama/ptrace_scope'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	stdout, stderr = out.communicate()
	return False if '0' in stdout.decode("utf-8") else True


def problem_ptrace():
	text = ("Ptrace is a mechanism that allows one process to 'trace' the execution "
	"of another process,  the legitimate use case for this functionality is "
	"debugging, malicious implants sometimes use this functionality to steal "
	"secrets from another process or to force them into serving as proxies for "
	"anomalous behavior.\n")
	print(open_red + text + close)


def mitigation_behavior_endpoint():
	text = ("Some endpoint security solutions can be configured to block "
	"some types of process injection based on common sequences of behavior "
	"that occur during the injection process.")
	print_mitigation(text)


def mitigation_privil_account():
	text = ("Utilize Yama to mitigate ptrace based process injection by "
	"restricting the use of ptrace to privileged users only. Other "
	"mitigation controls involve the deployment of security kernel "
	"modules that provide advanced access control and process restrictions "
	"such as SELinux, grsecurity, and AppArmor "
	"(https://www.nsa.gov/Portals/70/documents/what-we-do/cybersecurity/professional-resources/csi-limiting-ptrace-on-production-linux-systems.pdf?ver=2019-05-16-151825-133).")
	print_mitigation(text)


def analyze():
	print_process_injection()
	if not check_protecion_ptrace():
		problem_ptrace()
		mitigation_privil_account()
	mitigation_behavior_endpoint()
