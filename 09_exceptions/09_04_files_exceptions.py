'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''

# words = []
#
# with open ("books/war_and_peace.txt", "r") as fin:
#     for line in fin.readlines():
#         line = line.rstrip()
#         words.append(line)
#     print(words)
#
# new_list = ""
# with open("books/crime_and_punishment.txt", "w") as fout:
#         fout.write(new_list)
#

words = []
words1 = []
words2 = []

def checking():

    with open ("books/war_and_peace.txt", "r") as fin:
        for word in fin.readlines():
            word = word.rstrip()
            words.append(word)
        print(words[0][1])

    with open ("books/pride_and_prejudice.txt", "r") as fin:
        for word in fin.readlines():
            word = word.rstrip()
            words2.append(word)
        print(words2[0][1])

    with open ("books/crime_and_punishment.txt", "r") as fin:
        try:
            for word in fin.readlines():
                word = word.rstrip()
                words1.append(word)
            print(words1[0][1])
        except IndexError as zde:
            print("There was an error: ", zde)

checking()


class my_check(Exception):
    def __init__(self, message):
        message = self.message

    def __str__(self):
        print("I found Prince!")



# for char in fin.readlines():
#     char = char.rstrip()
# if char == "Prince":
#     print("Hello")
#
# else:
#     print("nope")
