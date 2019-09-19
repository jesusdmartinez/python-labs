'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''

nums = [1, 2, 3, 4, 5]

def sum():
    lst = 0
    for i in nums:
        lst += i
    print(lst)

sum()
