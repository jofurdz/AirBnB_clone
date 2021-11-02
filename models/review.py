#!/usr/bin/python3
''' Model defines class Review'''


from models.base_model import BaseModel


class Review(BaseModel):
    '''Review class definition'''

    place_id = ""
    user_id = ""
    text = ""
