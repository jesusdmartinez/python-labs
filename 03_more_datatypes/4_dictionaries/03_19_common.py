'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. For example:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''


'''FOR THIS ONE IM HAVING TROUBLE UNDERSTANDING WHAT THE ** IS DOING TO THE DICT_3 CREATION.  ANY EASY TO UNDERSTAND EXPLANATION?"
dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}

for x in dict_2:
    if x in dict_1:
        dict_2[x] = dict_2[x] + dict_1[x]

dict_3 = {**dict_1, **dict_2}
print(dict_3)