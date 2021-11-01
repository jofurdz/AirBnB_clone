#!/usr/bin/python3
"""class FileStorage"""


from models.base_model import BaseModel


# import
import json


class FileStorage:
    """class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return object attribute dict"""

        return self.__objects

    def new(self, obj):
        """ create new dict item"""

        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes to JSON file"""

        newDict = {}
        for key, value in self.__objects.items():
            newDict[key] = value.to_dict()

        with open(self.__file_path, "w") as fd:
            json.dump(newDict, fd)

    def reload(self):
        """deserializes JSON file"""
        try:
            with open(self.__file_path, 'r') as jsonObj:
                all_json = json.load(jsonObj)
                for key in all_json:
                    self.__objects[key] = getattr(
                        models, all_json[key]['__class__'])(**all_json[key])
        except Exception:
            pass
