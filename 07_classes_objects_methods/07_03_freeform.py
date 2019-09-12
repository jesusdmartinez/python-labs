'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''
class Smoothie():
    def __init__(self, fruit=0, cups=0, color=0):
        self.fruit = fruit
        self.cups = cups
        self.color = color

    def __str__(self):
        return f"this is a {self.fruit} smoothie; it has {self.cups} cups and is {self.color}"

    def __add__(self, other):
        total_fruit = self.fruit + other.fruit
        total_cups = self.cups + other.cups
        total_color = self.color + other.color
        return f"this is a {total_fruit} smoothie; it has {total_cups} cups and is {total_color}"

ras_smooth = Smoothie(10, 20, 30)
straw_smooth = Smoothie(10, 10, 10)
print(ras_smooth)
print(straw_smooth)
print(ras_smooth + straw_smooth)











