#!/usr/bin/python3
"""links FileStorage to BaseModel"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
