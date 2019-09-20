'''
Re-write the following listcomp as a lambda expression.

'''

names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']
print([x.startswith('D') for x in names])

### Jesus code attempt.
new = lambda x: "True" if x[0] == 'D' else "False", names
print(list(new))



# locations = ["indonesia", "spain", "thailand", "mexico", "usa"]
#
# locations.sort(key = lambda name: name[-1])
# print(locations)

