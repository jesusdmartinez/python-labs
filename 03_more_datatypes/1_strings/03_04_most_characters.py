'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''
string1 = str(input("please input a string1"))
string2 = str(input("please input a string2"))
string3 = str(input("please input a string3"))

len1 = len(string1)
len2 = len(string2)
len3 = len(string3)

big = max(len1, len2, len3)

if big == len1:
    print(string1)
if big == len2:
    print(string2)
if big == len3:
    print(string3)
