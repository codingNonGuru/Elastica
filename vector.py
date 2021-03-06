import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __truediv__(self, factor):
        return Vector(self.x / factor, self.y / factor)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, factor):
        return Vector(self.x * factor, self.y * factor)

    def getLength(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalize(self):
        length = self.getLength()
        self.x /= length
        self.y /= length
        return length

    def dot(self, other):
        return self.x * other.x + self.y * other.y