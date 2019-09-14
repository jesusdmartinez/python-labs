'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''


def hello():
    words = []
    longest = []
    shortest = []

    long_list = []
    short_list = []

    with open('words.txt', 'r') as fin:
        #move the words in words list
        for word in fin.readlines():
            word = word.rstrip()
            words.append(word)

        for word in words:
            if len(longest) < len(word):
                longest = word
            if len(shortest) > len(words):
                shortest = word
        print(len(longest))
        print(len(shortest))

        for word in words:
            if (len(word) % 21 == 0):
                long_list.append(word)

            if (len(word) == 2):
                short_list.append(word)

    print(f"The shortest words are: {short_list}")
    print(f"The longest words are: {long_list}")
    print(f"This list has {len(words)} words.")

hello()