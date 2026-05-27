import math

class Vector:
    def __init__(self, x=0, y=0):
        """Initialize instance variables for the class."""
        self.x = x
        self.y = y
    
    def __repr__(self):
        """Define what string to return when Vector class is printed/repr."""
        return f'Vector({self.x!r}, {self.y!r})'
    
    def __abs__(self):
        "Define behavior of abs() square root of x**2 + y**2"
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        """Define behaviour of bool() built-in function."""
        return bool(abs(self))
    
    def __add__(self, other):
        """Define behaviour of addition operator +"""
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __sub__(self, other):
        """Define behaviour of substration operator -"""
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        """Define behaviour of multiplication operator * """
        return Vector(self.x * scalar, self.y * scalar)
    
v = Vector(2,3)
x = Vector(1,1)
print(v-x)
print(v)