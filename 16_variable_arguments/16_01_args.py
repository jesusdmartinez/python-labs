'''
Write a script with a function that demonstrates the use of *args.

'''

def make_pizza(*args):
    for topping in args:
        print(f"*{topping}")

make_pizza('tomatoes', 'mushrooms')