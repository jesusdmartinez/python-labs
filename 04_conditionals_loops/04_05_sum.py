'''
Take two numbers from the user, an upper and lower bound.
Using a loop, calculate the sum of all numbers from the lower bound to the upper bound.

For example, if a user enters 1 and 100, the output should be:

The sum is: 5050
'''

upper = 200
lower = 1
summed = 0

for i in range(lower,upper+1):
    summed = summed + i
print(summed)
