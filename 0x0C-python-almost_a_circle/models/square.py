#!/usr/bin/python3
'''Module contain Square that inherits from Rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class has some feature of square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''initialize the square with the same logic of rectangle'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''get size of square'''
        return self.width
    
    @size.setter
    def size(self, val):
        '''set val to size'''
        self.width = val
        self.height = val

    def __str__(self):
        '''string repersentaion of Square'''
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.width)
    
    def update(self, *args, **kwargs):
        '''
        Assigns an argument to each attribute
        Args:
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
        '''
        if args:
            for i in range(len(args)):
                match i:
                    case 0:
                        self.id = args[i]
                    case 1:
                        self.size = args[i]
                    case 2:
                        self.x = args[i]
                    case 3:
                        self.y = args[i]
        else:
           for key, value in kwargs.items():
                if key == 'size':
                   self.size = value 
                elif key == 'x':
                   self.x = value
                elif key == 'y':
                   self.y = value
                elif key == 'id':
                    self.id = value

    def to_dictionary(self):
        '''returns the dictionary representation of a Square'''
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

