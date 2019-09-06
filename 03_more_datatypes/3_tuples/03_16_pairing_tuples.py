'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

Notes:
If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

'''

'''JESUS NOTES:  I CAN SORT THE LIST BUT IM NOT QUITE SURE HOW TO CREATE PAIRS OF TUPLES WITHIN THE LIST... ANY IDEAS?'''
num_list = [4, 1, 6, 7, 12, 5]
num_list.sort()
num_tuple = tuple(num_list)
for x in num_list:
    print(tuple(num_list))










