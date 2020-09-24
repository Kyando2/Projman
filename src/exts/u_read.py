import os

import Kyandle

class Data:

    def __init__(self, is_none, data):
        self.__data = data
        self.__is_none = is_none
        self.__is_dict = False
        self.__is_list = False
        if isinstance(data, dict):
            self.__is_dict = True
        elif isinstance(data, list):
            self.__is_list = True

    def __len__(self):
        if self.__is_none:
            return 0
        else:
            return(len(self.__data))

    def __getitem__(self, key):
        if not self.__is_none:
            return self.__data[key]
        else:
            raise TypeError

    def __setitem__(self, key, value):
        if not self.__is_none:
            self.__data[key] = value
        else:
            raise TypeError

    def __iter__(self):
        if not self.__is_none:
            return self.__data.__iter__()
        else:
            raise TypeError

    def __contains__(self, item):
        if not self.__is_none:
            if item in self.__data: 
                return True
            return False
        else:
            raise TypeError

    def __str__(self):
        return str(self.__data)
    
    def __bool__(self):
        if not self.__is_none:
            return True
        else:
           return False

def read(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return Data(False, Kyandle.parse(f.read()))
    return Data(True, None)