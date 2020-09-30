#!/usr/bin/python3

from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation
from techniques.config.sudoers_permissions import read_permission
from techniques.config.sudoers_permissions import open_sudoers
from techniques.config.sudoers_permissions import sudoers

import os
import re


def print_sudo_message():
	text = "( Searching /etc/sudoers permissions )"
	print_title_technique(text)


def sudoers_permissions():	
	os.system("ls -la " + sudoers)
	print("\n")
	os.system("sudo -l")


def read_sudoers(content):
	text = ("[+] Misconfigurations in read permissions, reading file content.")
	print(open_red + text + close)
	print(content)


def check_nopasswd(content):
	# Check if exists NOPASSWD in a line without commenting
	regex = r"[^#]*NOPASSWD.*"
	if re.search(regex, content, re.MULTILINE):
		text = ("[+] Suspicious content due to NOPASSWD in " + sudoers + 
		", take a look and delete it if you can.\n")
		print(open_red + text + close)
		return True


def mitigation_nopasswd():
	text = ("Limits NOPASSWD permissions strictly to necessary binaries.")
	print_mitigation(text)


def mitigation_readable():
	text = ("The sudoers file should be strictly edited such that passwords "
	"are always required and that users can't spawn risky processes as "
	"users with higher privilege.")
	print_mitigation(text)


def mitigation_priv_acc_manag():
	text = ("By requiring a password, even if an adversary can get terminal "
	"access, they must know the password to run anything in the sudoers file.")
	print_mitigation(text)


def analyze():
	print_sudo_message()
	sudoers_permissions()
	bool_read_sudoers = read_permission()
	if bool_read_sudoers:
		content = open_sudoers()
		read_sudoers(content)
		mitigation_readable()
		mitigation_priv_acc_manag()
		if check_nopasswd(content):
			mitigation_nopasswd()
