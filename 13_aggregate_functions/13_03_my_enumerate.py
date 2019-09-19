'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

def my_enumerate():
    my_num = input("create a list of anything so I can enumerate")
    new_num = my_num.split()
    print(list(enumerate(new_num)))

my_enumerate()