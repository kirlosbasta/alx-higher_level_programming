#!/usr/bin/python3
'''
write a function that returns the JSON representation of an object (string):

Prototype: def to_json_string(my_obj):
You don’t need to manage exceptions if the object can’t be serialized.
'''
import json

def to_json_string(my_obj):
    '''returns the JSON representation of an my_obj'''
    return json.dumps(my_obj)
