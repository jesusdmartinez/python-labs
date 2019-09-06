'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

shift = 0
while not int(shift) in range(1,1000000000):
    shift = input("Please enter your shift (1 - 1,000,000,000) : ")

    if int(shift) % 3 == 0:
        print("yes")

    else:
        print("nope")

print(int(shift) % 3)

