'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

words = []
words_reverse = []

with open('words.txt', 'r') as fin:
    for word in fin.readlines():
        word = word.rstrip()
        words.append(word)

    words_reverse = words[::-1]

print(words_reverse)

with open("words_reverse.txt", "w") as fout:
    fout.write("\n".join(words_reverse))

    #this doesn't work... i wonder why?
    # for word in words:
    #     new = ""
    #     new = word + new
    #     print(new)
