'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''


while True:
    try:
        num1 = int(input("tell me a number bro"))
        num2 = int(input("tell me a number dude"))
        print(num1 / num2)
        break
    except ZeroDivisionError as zde:
        print("can't divide by zero dude:", zde)

    except ValueError as zde:
        print("you need a number dude:", zde)