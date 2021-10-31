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

    def do_create(self, arg):
        """creates a new instance of basemodel"""
        if arg == "" or None:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            newModel = BaseModel()
        print(newModel.id)

    def do_show(self, arg):
        """prints string representation of an instance"""
        if not args:
            return print("** class name missing **")
        try:
            getatr(models, args.split(" ")[0])
        except Exception:
            return print("** class doesn't exist **")
        if len(args.split(" ")) < 2:
            return print("** instance id missing **")

    def do_destroy(self, args):
        """deletes instance based on class name and id"""

        className = None
        classID = None
        if arg != "":
            try:
                className = arg.split(" ")[0]
                classID = arg.split(" ")[1]
            except IndexError:
                pass
            if className is None:
                print("** class name missing **")
            elif className not in ["Amenity", "BaseModel", "City",
                                   "Place", "Review", "State", "User"]:
                print("** class doesn't exist **")
            elif classID is None:
                print("** instance id missing **")
            else:
                objName = className + "." + classID
                delete = None
                all_objs = storage.all()
                for key in all_objs.keys():
                    if key == objName:
                        delete = key
                    if delete is not None:
                        all_objs.pop(delete)
                        sorage.save()
                    else:
                        print("** no instance found **")

    def do_all(self, arg):
        """prints all string representation of all instances"""
        obj_list = []
        if arg == "":
            all_objs = storage.all()
            for key in all_objs.values():
                obj_list.append(key.__str__())
            print(obj_list)
        elif arg not in ["Amenity", "BaseModel", "City",
                         "Place", "Review", "State", "User"]:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            for key in all_objs.values():
                if key.__class__.__name__ == arg:
                    obj_list.append(key.__str__())
            print(obj_list)

    def do_update(self, args):
        """updates instance based on class name and ID"""


if __name__ == "__main__":
    HBNBCommand().cmdloop()
