#!/usr/bin/python3
"""This defines a class Student"""


class Student:
    """This represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student

        Args:
            first_name (str): Student first name
            last_name (str): Student last name
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student"""
        return self.__dict__
