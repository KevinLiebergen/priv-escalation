#!/usr/bin/python3

from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation

import os
import urllib.request


def print_web_shell_message():
	text = "( Web Shell )"
	print_title_technique(text)


def check_if_web_server():
	try:
		if urllib.request.urlopen("http://127.0.0.1").getcode(): return True
	except:
		return False

def dangerous_users():
	print(open_green + "\nUsers with ID = 0 and admin rights:" + close)
	os.system("awk -F: '($3 == 0) {print}' /etc/passwd")	


def print_groups():
	print(open_green + "\nSystem groups:" + close)
	os.system("getent group")


def active_services():
	print(open_green + "\nScanning for active services:" + close)
	os.system("systemctl | grep running")


def print_no_web_server():
	print(open_green + "There is no web server running.\n" + close)


def web_server_information():
	text = "Searching information about Web Server and system."
	print(open_green + text + close)
	dangerous_users()
	print_groups()
	active_services()


def users_with_shell():
	print(open_green + "\nSearching users with shell.\n" + close)
	os.system('getent passwd | grep ".*sh$"')


def check_web_shell_vulns():
        web_server_information()
        users_with_shell()
        mitigation_update_sw()
        mitigation_privil_account()


def mitigation_privil_account():
	text = ("Audit account and group permissions to ensure that accounts "
	"used to manage servers do not overlap with accounts and permissions "
	"of users in the internal network that could be acquired through "
	"Credential Access and used to log into the Web server and plant a "
	"Web shell or pivot from the Web server into the internal network.")
	print_mitigation(text)


def mitigation_update_sw():
	text = ("Ensure that externally facing Web servers are patched "
	"regularly to prevent adversary access through Exploitation for "
	"Privilege Escalation to gain remote code access or through file "
	"inclusion weaknesses that may allow adversaries to upload files "
	"or scripts that are automatically served as Web pages.")
	print()
	print_mitigation(text)


def analyze():
	print_web_shell_message()
	if check_if_web_server():
                check_web_shell_vulns()
	else:
		print_no_web_server()
