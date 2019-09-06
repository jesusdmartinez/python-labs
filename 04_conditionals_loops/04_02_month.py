'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

month = 0
while not int(month) in range(1,13):
    month = input("Enter the number of a month")

if int(month) == 1:
    print("January")

if int(month) == int(2):
    print("February")

if int(month) == int(3):
    print("March")

if int(month) == int(4):
    print("April")

if int(month) == int(5):
    print("May")

if int(month) == int(6):
    print("June")

if int(month) == int(7):
    print("July")

if int(month) == int(8):
    print("August")

if int(month) == int(9):
    print("September")

if int(month) == int(10):
    print("October")

if int(month) == int(11):
    print("November")

if int(month) == int(12):
    print("December")