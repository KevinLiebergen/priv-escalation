#!/usr/bin/python3

from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation
from techniques.config.sudoers_permissions import read_permission
from techniques.config.sudoers_permissions import open_sudoers

import re


def print_sudo_caching_message():
	text = "( Sudo caching )"
	print_title_technique(text)


def check_tty_tickets(content):
		# Regex to find line that begins with Defaults and then include !tty_tickets
		regex = r"^Defaults[^#]*!tty_tickets"

		if re.search(regex, content, re.MULTILINE):
			text = ("[+] The tty_tickets are disabled, the sudo timeout of one "
			"tty will afect another tyy (you won't have to type the password again "
			"if you are in the timestamp_timeout).")
			print(open_red + text + close) 
			return True


def check_timestamp(content):
	# Search for timestamp_timeout=0 and is not commented
	regex = r"^Defaults[^#]*timestamp_timeout=0"
	if not re.search(regex, content, re.MULTILINE):
		text = ("\n[+] Exists an amount of time in minutes between instances of "
		"sudo before it will re-prompt for a password, an malware can execute sudo "
		"commands without needing to supply the users's password.")
		print(open_red + text + close)
		return True


def mitigation_tty():
	text = ("Ensuring that the tty_tickets setting is enabled will prevent this leakage "
	"across tty sessions.")
	print_mitigation(text)


def mitigation_timestamp():
	text = ("Setting the timestamp_timeout to 0 will require the user to input their " 
	"password every time sudo is executed.")
	print_mitigation(text)
	

def analyze():
	print_sudo_caching_message()
	bool_read_sudoers = read_permission()
	if bool_read_sudoers:
		content = open_sudoers()
		if check_tty_tickets(content):
			mitigation_tty()

		if check_timestamp(content):
			mitigation_timestamp()
