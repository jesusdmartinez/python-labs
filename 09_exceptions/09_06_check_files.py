'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

file_name = 'integers.txt'
min = []

with open("integers.txt", "r") as fin:
    for num in fin.readlines():
        num = num.rstrip()
        min.append(num)
    my_num = int(min[0])

while True:

    try:
        new_num = int(input("Put a new num g:"))
        print(my_num / new_num)
        break

    except ValueError as zde:
        print("There is an errorV: ", zde)
    except IOError as zde:
        print("There is an errorI: ", zde)
    except ZeroDivisionError as zde:
        print("There is an errorZ: ", zde)


