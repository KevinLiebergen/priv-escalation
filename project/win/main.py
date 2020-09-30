from techniques import access_token_manipulation
from techniques import accesibility_features
from techniques import application_shiming
from techniques import appcert_dlls
from techniques import appinit_dlls
from techniques import bypass_user_account
from techniques import dll_search_order
from techniques import exploitation
from techniques import extra_window_memory
from techniques import file_system_permissions
from techniques import hooking
from techniques import image_file_execution
from techniques import new_service
from techniques import parent_pid_spoofing
from techniques import path_interception
from techniques import port_monitors
from techniques import powershell_profile
from techniques import process_injection
from techniques import scheduled_task
from techniques import service_registry_permissions
from techniques import sid_history_injection
from techniques import valid_accounts
from techniques import web_shell

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

    access_token_manipulation.analyze()
    accesibility_features.analyze()
    application_shiming.analyze()
    appcert_dlls.analyze()
    appinit_dlls.analyze()
    bypass_user_account.analyze()
    dll_search_order.analyze()
#    exploitation.analyze(base_path=BASE_PATH)
    exploitation.analyze()
    extra_window_memory.analyze()
    file_system_permissions.analyze()
    hooking.analyze()
    image_file_execution.analyze()
    new_service.analyze()
    parent_pid_spoofing.analyze()
    path_interception.analyze()
    port_monitors.analyze()
    powershell_profile.analyze()
    process_injection.analyze()
    scheduled_task.analyze()
    service_registry_permissions.analyze()
    sid_history_injection.analyze()
    valid_accounts.analyze()
    web_shell.analyze()



if __name__ == "__main__":
        main()
