'''
Write a script that creates a list of all unique values in a list. For example:

list = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''


list = [1, 2, 6, 55, 2, 'hi', 4, 2, 6, 1, 13]
final_list = []

for i in list:
    if list.count(i) < 2:
        final_list.append(i)

print(final_list)