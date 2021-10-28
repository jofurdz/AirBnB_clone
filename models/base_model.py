#!/usr/bin/python3
"""class BaseModel"""

import uuid
from datetime import datetime
import time
import models


class BaseModel:
    """class BaseModel defines common sttributes for all classes"""

    def __init__(self, *args, **kwargs):
        """initializes object"""
        if kwargs:
            for key, value in kwargs.items():
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__[key] = value

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """prints class name and id"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """returns dictionary containing key values"""
        newDict = dict(self.__dict__)
        newDict["__class__"] = self.__class__.__name__
        newDict["created_at"] = self.created_at.isoformat()
        newDict["updated_at"] = self.updated_at.isoformat()

        return newDict


    def save(self):
        """updates public instance with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()
