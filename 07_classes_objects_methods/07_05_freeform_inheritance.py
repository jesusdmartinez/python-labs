'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

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

class Vegetable(Smoothie):
    def __init__(self, fruit=0, cups=0, color=0, vegetable=10):
        super().__init__(fruit, cups, color)
        self.vegetable = vegetable

    def __str__(self):
        return f"this is a {self.fruit} smoothie; it has {self.cups} cups and is {self.color} and has {self.vegetable} veggies"

veg_smooth = Vegetable()
ras_smooth = Smoothie(10, 20, 30)
straw_smooth = Smoothie(10, 10, 10)

print(ras_smooth)
print(straw_smooth)
print(veg_smooth)
print(ras_smooth + straw_smooth)