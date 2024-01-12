#!/usr/bin/python3
'''
class will be the “base” of all other classes
in this project
'''


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
