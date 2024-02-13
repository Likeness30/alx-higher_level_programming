#!/usr/bin/python3
"""A module that defines a base class for other classes."""


import json
import os.path
import csv


class Base:
    """This represents the Base class for all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance with optional ID"""

        if id is not None:
            if not isinstance(id, int):
                raise TypeError("id must be an integer")
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):


        if not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class type")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        if os.path.isfile(filename):
            return [cls.create(**dictionary)
                    for dictionary in cls.from_json_string(open(filename).read())]
        else:
            return []


    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = f"{cls.__name__}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"
        if not os.path.isfile(filename):
            return []

        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            objs = []
            for row in reader:
                if cls.__name__ == "Rectangle":
                    objs.append(cls.create(id=int(row[0]), width=int(row[1]),
                        height=int(row[2]), x=int(row[3]), y=int(row[4])))
                elif cls.__name__ == "Square":
                    objs.append(cls.create(id=int(row[0]), size=int(row[1]),
                        x=int(row[2]), y=int(row[3])))
            return objs
