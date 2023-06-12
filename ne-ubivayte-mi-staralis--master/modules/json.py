import json
import os
import modules.search_path as m_path

def create_json(name_dict):
    with open(m_path.path_search(name_dict["login"]),"w") as file:
        json.dump(name_dict, file)

def read_json(name_dict):
    with open(m_path.path_search(name_dict["login"],"r")) as file:
        json.load(file)
