'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet():
    def __init__(self, name, color, system):
        self.name = name
        self.color = color
        self.system = system

    def __str__(self):
        return f"this planet is called {self.name}, it is {self.color} and is in the {self.system} solar system"

mars = Planet('mars', 'red', 'solar')
print(mars)
