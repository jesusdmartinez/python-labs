'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def make_pizza(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} mapsa to {v}")

make_pizza(dough='wheat', topping='tomatoes')