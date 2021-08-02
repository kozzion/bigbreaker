import random
import string
import json
import sys
import os
import pathlib

sys.path.append('../')
from bigbreaker.instagram.pagemanager_instagram import PagemanagerInstagram
from bigbreaker.common.system_webdriver import SystemWebdriver

path_file_executable = 'C:\\project\\chromedriver_win32\\chromedriver.exe'

path_file_session = 'session.json'
path_file_identity = 'identity.json'
path_dir_user_data = os.path.join(str(pathlib.Path().absolute()), 'selenium')

system_webdriver = SystemWebdriver(path_file_executable)
driver = system_webdriver.get_webdriver(path_file_session, path_dir_user_data)



def create_identity():
    size_password = 12
    with open('list_first_name.txt', encoding='ascii', errors='ignore') as file:
        list_name_first = file.readlines()
    with open('list_first_name.txt', encoding='ascii', errors='ignore') as file:
        list_name_last = file.readlines()
    identity = {}
    identity['name_first_0']  = random.choice(list_name_first).strip()
    identity['name_last_0']   = random.choice(list_name_last).strip()
    identity['onionmail_username'] = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=size_password))
    identity['onionmail_address']  = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=size_password))
    identity['onionmail_password'] = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=size_password))
    return identity

if os.path.isfile(path_file_identity):
    with open(path_file_identity, 'r') as file:
        identity = json.load(file)
else:
    identity = create_identity()
    with open(path_file_identity, 'w') as file:
        json.dump(identity, file)\
            
page_manager = PagemanagerOnionmail(driver)
# page_manager.action_create_account()
# page_manager.action_login(identity)
page_manager.action_get_email_most_recent(identity)

#<input type="text" class="form-control" name="name" id="name" placeholder="eg. &quot;Jaan Tamm&quot;" value="" required="">
