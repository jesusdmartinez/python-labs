'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
input = "hello world"
result_list = []
new_list = input.split()
print(new_list)

for word in new_list:
        result_list.append(tuple(word))
print(result_list)

