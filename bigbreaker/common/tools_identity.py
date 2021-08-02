import os
import sys
import json
import random
import string

from bigbreaker.common.system_webdriver import SystemWebdriver

class ToolsIdentity:

    def identity_create(config, id_identity, random_seed = None):
        path_dir_data = config['path_dir_data']
        path_file_list_name_first = os.path.join(path_dir_data, 'list_first_name.txt')
        path_file_list_name_last = os.path.join(path_dir_data, 'list_first_name.txt')
        path_file_identity = os.path.join(path_dir_data, 'identity', id_identity, 'identity.json')

        size_password = 12
        with open(path_file_list_name_first, encoding='ascii', errors='ignore') as file:
            list_name_first = file.readlines()
        with open(path_file_list_name_last, encoding='ascii', errors='ignore') as file:
            list_name_last = file.readlines()
        if random_seed:
            random.random.seed = random_seed

        identity = {}
        identity['id_identity'] = id_identity
        identity['name_first_0']  = random.choice(list_name_first).strip()
        identity['name_last_0']   = random.choice(list_name_last).strip()
        identity["name_full"]  = identity["name_first_0"] + " " + identity["name_last_0"]
        identity['onionmail_is_created'] = False
        identity['onionmail_username'] = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=size_password))
        #identity['onionmail_address']  = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=size_password))
        identity['onionmail_password'] = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=size_password))

        identity['instagram_username'] = identity['name_first_0'] + '_' +''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=6))
        identity['instagram_password'] = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=size_password))

        with open(path_file_identity, 'w') as file:
            json.dump(identity, file)

        return identity

    def identity_load(config, id_identity):
        path_dir_data = config['path_dir_data']
        path_file_identity = os.path.join(path_dir_data, 'identity', id_identity, 'identity.json')
        with open(path_file_identity, 'r') as file:
            return json.load(file)

    def identity_save(config, id_identity, identity):
        if not identity['id_identity'] == id_identity:
            raise Exception()

        path_dir_data = config['path_dir_data']
        path_file_identity = os.path.join(path_dir_data, 'identity', id_identity, 'identity.json')
        with open(path_file_identity, 'w') as file:
            json.dump(identity, file)

    def webdriver_load(config, id_identity):
        path_dir_data = config['path_dir_data']
        path_file_webdriver = config['path_file_webdriver']
        path_file_session = os.path.join(path_dir_data, 'identity', id_identity, 'session.json')
        path_dir_user_data = os.path.join(path_dir_data, 'identity', id_identity, 'selenium')
        system_webdriver = SystemWebdriver(path_file_webdriver)
        driver = system_webdriver.get_webdriver(path_file_session, path_dir_user_data)
        
