'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

string = str(input("please input a string"))
symbol = str(input("please input a symbol"))
replace = string[:1]
print(string.replace(replace, symbol))
