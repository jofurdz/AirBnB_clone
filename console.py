#!/usr/bin/python3
"""console for AirBnB project"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """console for AirBnB project"""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """exits console"""
        exit()

    def do_quit(self, arg):
        """exits console"""
        exit()

    def emptyLine(self):
        """handles empty line"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
