'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results

def multiple(m):
	return print("DIVISIBLE by 4 or 7 yo") if m % 4 == 0  or m % 7 == 0 else print("NOT divisible by 4 or 7 yo")

def multiple_both(m):
	return print("its both bro") if m % 4 == 0  and m % 7 == 0 else print("one or the other!")

user_input = 0

while not int(user_input) in range(1, 1000000):
    user_input = input("tell me a number between 0 and 1,000,000")

multiple(int(user_input))
multiple_both(int(user_input))


