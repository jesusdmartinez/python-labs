'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''


words = []

with open('words.txt', 'r') as fin:
    for word in fin.readlines():
        word = word.rstrip()
        words.append(word)


long_list = []

for word in words:
    if len(word) >= 20:
        long_list.append(word)



print(long_list)
print("\n".join(long_list))


with open("long.txt", "w") as fout:
    fout.write("\n".join(long_list))




