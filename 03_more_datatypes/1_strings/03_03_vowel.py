'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''

string = str(input("please input a string"))
a = string.count('a')
e = string.count('e')
i = string.count('i')
o = string.count('o')
u = string.count('u')
print(a + e + i + o + u)