'''
Write a script that demonstrates a try/except/else.

'''

try:
    num1 = int(input("tell me a number"))
    num2 = int(input("tell me another"))

except ZeroDivisionError as zde:
    print("cant divide by zero yo", zde)

except ValueError as zde:
    print("it's wrong", zde)

else:
    print(f"Your done bro:  {num1} / {num2}")