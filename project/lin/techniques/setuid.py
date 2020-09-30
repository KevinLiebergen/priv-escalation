#!/usr/bin/python3

from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import close
from techniques.config.utilities import print_title_technique
from techniques.config.utilities import print_mitigation

import os


def print_uid_message():
	text = "( Searching files with bit setuid activated )"
	print_title_technique(text)


def print_gid_file_message():
	text = "( Searching files with setgid activated )"
	print_title_technique(text)


def print_gid_directory_message():
	text = "( Searching directories with setgid activated )"
	print_title_technique(text)


def search_uid():
	print_uid_message()
	os.system("find / -user root -perm /4000 -exec ls -l {} \; 2> /dev/null")


def search_gid_files():
	print_gid_file_message()
	os.system("find / -user root -type f -perm /2000 -exec ls -l {} \; 2> /dev/null")


def search_gid_directories():
	print_gid_directory_message()
	os.system("find / -user root -type d -perm /2000 -exec ls -ld {} \; 2> /dev/null")


def mitigation_setuid_setgid():
	text = ("Applications with known vulnerabilities or known shell escapes should not "
	"have the setuid or setgid bits set to reduce potential damage if an application "
	"is compromised. Additionally, the number of programs with setuid or setgid bits "
	"set should be minimized across a system.")
	print()
	print_mitigation(text)


def analyze():
	search_uid()
	search_gid_files()
	search_gid_directories()

	mitigation_setuid_setgid()
