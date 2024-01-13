#!/usr/bin/python3
'''
class will be the “base” of all other classes
in this project
'''
import json


class Base:
    '''The base of all other class to come in this project'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''initialze id for all the inistance'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of
        list_dictionaries'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
