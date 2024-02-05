#!/usr/bin/python3
"""This defines an  object attributes lookup functiom"""


def lookup(obj):
    """Return a list of an objects available attributes"""
    return (dir(obj))
