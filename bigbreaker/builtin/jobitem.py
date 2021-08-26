
import os
import sys
import json

class Company:

    @staticmethod
    def jobitem_save(config, id_jobitem, json_jobitem):
        path_dir_data = config['path_dir_data']  
        path_file_jobitem = os.path.join(path_dir_data, 'builtin', 'jobitem', id_jobitem, 'jobitem.json')
        with open(path_file_jobitem, 'w') as file:
            json.dump(json_jobitem, file)

    @staticmethod
    def jobitem_load(config, id_jobitem):
        path_dir_data = config['path_dir_data']  
        path_file_jobitem = os.path.join(path_dir_data, 'builtin', 'jobitem', id_jobitem, 'jobitem.json')
        with open(path_file_jobitem, 'r') as file:
            return json.load(file)

            