#!/usr/bin/python3
''' Model w/ class City'''

from models.base_model import BaseModel

class City(BaseModel):
    '''City class'''
    def __init__(self, *args, **kwargs):
        """initialize city"""
        state_id = ""
        name = ""
        super().__init__(*args, **kwargs)
