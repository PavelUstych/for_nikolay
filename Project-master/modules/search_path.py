import os

def create_path(name_file):
    path_abs = os.path.abspath(__file__ + "/..")
    path_abs = path_abs.split("\\") 
    del path_abs[-1]
    path_abs = "\\".join(path_abs)
    path_abs = os.path.join(path_abs, name_file)
    return path_abs