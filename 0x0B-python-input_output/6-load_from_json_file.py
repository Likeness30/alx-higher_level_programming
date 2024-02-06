#!/usr/bin/python3
"""This defines a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """It creates a Python object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
