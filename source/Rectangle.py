class Rectangle():

    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height

    def perimeter(self):
        return 2 * (self.length + self.height)
