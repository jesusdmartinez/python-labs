'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

say = "BLAHH"
say_counts = []

for i in say:
    say_counts.append(say.count(i))

print(say)
print(say_counts)

dictionary = dict(zip(say, say_counts))
print(dictionary)





