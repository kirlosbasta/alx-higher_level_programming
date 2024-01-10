#!/usr/bin/python3
'''Student to JSON'''


class Student:
    '''class Student that defines a student'''
    def __init__(self, first_name, last_name, age):
        '''initialize first_name, last_name, age'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        retrieves a dictionary representation of a Student instance
        '''
        if attrs is not None:
            new_dict = {key: self.__dict__[key] for key in attrs
                        if key in self.__dict__}
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        '''replaces all attributes of the Student instance'''
        if 'first_name' in json:
            self.first_name = json['first_name']
        if 'last_name' in json:
            self.last_name = json['last_name']
        if 'age' in json:
            self.age = json['age']
