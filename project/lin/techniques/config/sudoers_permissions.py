import os

sudoers = "/etc/sudoers"


def read_permission():
	return os.access(sudoers, os.R_OK)


def open_sudoers():
    file = open(sudoers, "r")
    if file.mode == "r":
        return file.read()

