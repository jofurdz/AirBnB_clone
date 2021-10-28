#!/usr/bin/python3
"""class FileStorage"""

#import
import json

class FileStorage:
    """class FileStoarge"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return object attribute dict"""
    
        return __objects
    
    def new(self, obj):
