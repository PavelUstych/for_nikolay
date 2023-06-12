import os
import json

def find_path_to_file(name_file):
    path = __file__.split("/")
    del path[-1]
    path = "/".join(path)
    path = os.path.join(path, name_file)
    return name_file

def create_json(name_dict):
    with open(find_path_to_file(name_dict['name']), 'w') as file:
        json.dump(name_dict, file, ensure_ascii= False, indent= 4) 

def read_json(name_dict):
    with open(find_path_to_file(name_dict['name']), 'r') as file:  
        return json.load(file)