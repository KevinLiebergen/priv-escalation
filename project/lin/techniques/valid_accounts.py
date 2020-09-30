#!/usr/bin/python3

from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation

import os

def print_valid_message():
	text = "( Searching Valid Accounts )"
	print_title_technique(text)
	
	
def search_possible_passwords():
	# Search in logs, history, words like passwords, passwd/s, pass, etc
	text = ("Finding possible passwords inside some critical files (_history, "
	".sudo_as_admin_successful, .profile, .bashrc, httpd.conf, .plan, .htpasswd, "
	".gitconfig, .git-credentials, .git, .svn, .rhost, hosts.equiv, Dockerfile, "
	"docker-compose.yml)\n")
	print(open_green + text + close)

	possible_pass = False

	files = ['*_history', '*.sudo_as_admin_successful', '*.profile', 
	'*bashrc', '*httpd.conf', '*.plan', '*.htpasswd', '*.gitconfig', 
	'*.git-credentials', '*.git', '*.svn', '*.rhost', '*hosts.equiv', 
	'*Dockerfile', '*docker-compose.yml'] 
	for file in files:
		# Find if specific files exists and grep to search pwd|password|passw with : or =
		command = "find / -name " + file + " -type f -exec egrep -nir -H --color '(api|psswd|pwd|password|passw|passwd)' {} \; 2> /dev/null"
		#command = "find / -name " + file + " -type f -exec egrep -nir -H --color '(api|pwd|password|passw)(\s)?(:|=)' {} \; 2> /dev/null"
		if os.system(command) != None: possible_pass = True
	
	return possible_pass
	
	
def search_ssh_keys():
	print(open_green + "\nSearching some ssh files\n" + close)
	exist_ssh_files = False
	if os.system('find / -name "*pub" 2> /dev/null') != None: exist_ssh_files = True
	if os.system('find / -name "*.ssh" 2> /dev/null') != None: exist_ssh_files = True
	if os.system('find / -name "*id_rsa" 2> /dev/null') != None: exist_ssh_files = True
	 
	return exist_ssh_files


def mitigation_app_dev_guidance():
	text = ("Ensure that applications do not store sensitive data or "
	"credentials insecurely. (e.g. plaintext credentials in code, "
	"published credentials in repositories, or credentials in public "
	"cloud storage).")
	print_mitigation(text)


def mitigation_password_policies():
	text = ("Applications and appliances that utilize default username and "
	"password should be changed immediately after the installation, "
	"and before deployment to a production environment. When possible, "
	"applications that use SSH keys should be updated periodically and "
	"properly secured.")
	print_mitigation(text)


def mitigation_priv_account_manag():
	text = ("Audit domain and local accounts as well as their permission "
	"levels routinely to look for situations that could allow an adversary "
	"to gain wide access by obtaining credentials of a privileged account. "
	"These audits should also include if default accounts have been enabled, "
	"or if new local accounts are created that have not be authorized. "
	"Follow best practices for design and administration of an enterprise "
	"network to limit privileged account use across administrative tiers.")
	print_mitigation(text)


def analyze():
	print_valid_message()
	if search_possible_passwords():
		mitigation_app_dev_guidance()
	
	if search_ssh_keys():
		mitigation_password_policies()
