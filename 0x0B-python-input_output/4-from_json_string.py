#!/usr/bin/python3
"""This defines a JSON-to-object function"""
import json


def from_json_string(my_str):
    """It returns the Python object rep. of a JSON string"""
    return json.loads(my_str)
