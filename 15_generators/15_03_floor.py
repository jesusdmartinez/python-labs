'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''

list = [1111, 2222, 3333, 30]

gen = (x for x in list if x % 1111 == 0)

for x in gen:
    print(x // 1111)