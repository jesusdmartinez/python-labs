'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

def mine():
    while True:
        try:
            number = int(input("Please enter a number"))
            print(f"Your number is ~{number}!")
            break

        except ValueError as zde:
            print("Enter an integer please: ", zde)

mine()

