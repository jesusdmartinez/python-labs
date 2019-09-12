'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

    def perimiter(self):
        print(self.width*2 + self.length*2)

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(3.14*self.radius*self.radius)

    def circumference(self):
        print(2*3.14*self.radius)

rec = Rectangle(5, 10)
rec.area()
rec.perimiter()

cir = Circle(5)
cir.area()
cir.circumference()





