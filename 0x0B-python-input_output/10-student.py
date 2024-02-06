#!/usr/bin/python3
"""This defines a class Student"""


class Student:
    """This represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): Student first name
            last_name (str): Student last name
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student

        If attrs is a list of strings, represents only those attributes
        included in the list

        Args:
            attrs (list): (Optional) The represented attributes
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
