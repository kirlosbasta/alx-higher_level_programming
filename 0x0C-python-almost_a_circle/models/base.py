#!/usr/bin/python3
'''
class will be the “base” of all other classes
in this project
'''
import json
import turtle


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

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes the JSON string representation
        of list_objs to a file'''
        with open('{}.json'.format(cls.__name__), 'w', encoding='utf-8') as f:
            if list_objs is None or len(list_objs) == 0:
                json_strings = "[]"
            else:
                json_objs = [obj.to_dictionary() for obj in list_objs]
                json_strings = cls.to_json_string(json_objs)
            f.write(json_strings)

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation json_string'''
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        ''' returns a list of instances loaded from json file'''
        try:
            with open('{}.json'.format(cls.__name__), 'r',
                      encoding='utf-8') as f:
                json_str = f.read()
                list_output = cls.from_json_string(json_str)
                list_instance = []
                for dic in list_output:
                    list_instance.append(cls.create(**dic))
                return list_instance
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''same bevaiour as save_to_file'''
        import csv
        with open('{}.csv'.format(cls.__name__), 'w', encoding='utf-8') as f:
            if cls.__name__ == 'Rectangle':
                fieldsname = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == 'Square':
                fieldsname = ['id', 'size', 'x', 'y']
            csv_write = csv.DictWriter(f, fieldnames=fieldsname)
            csv_write.writeheader()
            if list_objs is None or len(list_objs) == 0:
                return
            else:
                for obj in list_objs:
                    csv_write.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        '''load the data from csv to list of inistance of that class'''
        import csv
        try:
            with open('{}.csv'.format(cls.__name__), 'r',
                      encoding='utf-8') as f:
                csv_read = csv.DictReader(f)
                list_instance = []
                for dic in csv_read:
                    dic = {key: int(dic[key]) for key in dic}
                    list_instance.append(cls.create(**dic))
                return list_instance
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''draw rectangle and square from each list respectively'''
        t = turtle.Turtle()
        t.color('blue', 'cyan')
        turtle.getscreen().bgcolor('#555F40')
        for rec in list_rectangles:
            t.pu()
            t.goto(rec.x, rec.y)
            t.pd()
            for i in range(2):
                t.fd(rec.width * 2)
                t.lt(90)
                t.fd(rec.height * 2)
                t.lt(90)
        for sq in list_squares:
            t.pu()
            t.goto(sq.x, sq.y)
            t.pd()
            for i in range(4):
                t.fd(sq.size * 2)
                t.lt(90)
        turtle.done()
