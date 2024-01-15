#!/usr/bin/python3
'''Module contain Rectangle that inherits from Base'''



class Rectangle(Base):
    '''set some feature of rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''initialize some basic feature of rectangle'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''return the width'''
        return self.__width

    @width.setter
    def width(self, val):
        '''assign width'''
        if type(val) is not int:
            raise TypeError('width must be an integer')
        elif val <= 0:
            raise ValueError('width must be > 0')
        self.__width = val

    @property
    def height(self):
        '''return the height'''
        return self.__height

    @height.setter
    def height(self, val):
        '''assign height'''
        if type(val) is not int:
            raise TypeError('height must be an integer')
        elif val <= 0:
            raise ValueError('height must be > 0')
        self.__height = val

    @property
    def x(self):
        '''return the x'''
        return self.__x

    @x.setter
    def x(self, val):
        '''assign x'''
        if type(val) is not int:
            raise TypeError('x must be an integer')
        elif val < 0:
            raise ValueError('x must be >= 0')
        self.__x = val

    @property
    def y(self):
        '''return the y'''
        return self.__y

    @y.setter
    def y(self, val):
        '''assign y'''
        if type(val) is not int:
            raise TypeError('y must be an integer')
        elif val < 0:
            raise ValueError('y must be >= 0')
        self.__y = val

    def area(self):
        '''Return the area of rectangle'''
        return self.width * self.height

    def display(self):
        '''display the recatngle using #'''
        if self.width == 0 or self.height == 0:
            return
        rec = ""
        rec += '\n' * self.y
        for i in range(self.height):
            rec += ' ' * self.x
            for j in range(self.width):
                rec += '#'
            if i != self.height - 1:
                rec += '\n'
        print(rec)

    def __str__(self):
        '''string repersentaion of Rectangle'''
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        '''
        Assigns an argument to each attribute
        Args:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        '''
        if args:
            for i in range(len(args)):
                match i:
                    case 0:
                        self.id = args[i]
                    case 1:
                        self.width = args[i]
                    case 2:
                        self.height = args[i]
                    case 3:
                        self.x = args[i]
                    case 4:
                        self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
                elif key == 'id':
                    self.id = value

    def to_dictionary(self):
        ''' returns the dictionary representation of a Rectangle'''
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
