#!/usr/bin/python3

from techniques import setuid
from techniques import sudo_caching
from techniques import sudo
from techniques import valid_accounts
from techniques import web_shell
from techniques import process_injection
from techniques import exploitation

import os
import sys

def greet():
	print('''
            _                                _       _   _             
 _ __  _ __(_)_   __      ___  ___  ___ __ _| | __ _| |_(_) ___  _ __  
| '_ \| '__| \ \ / /____ / _ \/ __|/ __/ _` | |/ _` | __| |/ _ \| '_ \ 
| |_) | |  | |\ V /_____|  __/\__ \ (_| (_| | | (_| | |_| | (_) | | | |
| .__/|_|  |_| \_/       \___||___/\___\__,_|_|\__,_|\__|_|\___/|_| |_|
|_|                                                             
                                         Made with <3 by KevinLiebergen 

	''')


def main():
    BASE_PATH = "/".join(os.path.abspath(sys.argv[0]).split('/')[:-1])
    greet()

    exploitation.analyze(base_path=BASE_PATH)
    process_injection.analyze()
    setuid.analyze()
    sudo.analyze()
    sudo_caching.analyze()
    valid_accounts.analyze()
    web_shell.analyze()


if __name__ == "__main__":
	main()
