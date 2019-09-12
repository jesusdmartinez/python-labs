'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car():
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def accelerate(self):
        self.max_speed += int(5)

    def __str__(self):
        return f"your car is a {self.year} {self.model} that rips at {self.max_speed} mph!"

lambo = Car('labo', 2010, 300)
tesla = Car('tesla', 2019, 400)

lambo.accelerate()
lambo.accelerate()

tesla.accelerate()

print(lambo, tesla)


