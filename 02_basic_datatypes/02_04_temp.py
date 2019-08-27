'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''
F = int(input("Please input a degree in fahrenheit"))
C = ((F - 32) * (5/9))
print("{} degrees farenheit = {} degrees celsius".format(int(F), int(C)))




