'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
# input_string = input("Enter a 10 numbers separated by space yo ")
# list  = input_string.split()
# print(max(list))


my_list = [3, 5, 7, 8]
product = 1
for i in my_list:
    product = product * i

print(product)




