#!/usr/bin/python3
"""Square module that inherits from a class Rectangle """


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of Square instance"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates the attributes of the square """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args[:4]):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of the square """
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
