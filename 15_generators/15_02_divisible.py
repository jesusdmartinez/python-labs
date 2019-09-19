'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

list = [1111, 2222, 333, 30]

gen = (x for x in list if x % 1111 == 0)

for x in gen:
    print(x)

