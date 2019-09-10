'''
Write a script that takes in a list and finds the max, min, average and sum.

'''

list = []
for i in range(0, 3):
    new = int(input("enter a 3 numbers"))
    list.append(new)

def newbie(x):
    print(max(list))
    print(min(list))
    print(sum(list) / len(list))
    print(sum(list))

newbie(list)