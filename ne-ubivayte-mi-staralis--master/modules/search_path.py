import os

def path_search(name_file):
    path = __file__.split("/")
    del path[-1]
    path = "/".join(path)
    path = os.path.join(path, name_file)
    return name_file