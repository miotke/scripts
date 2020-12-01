import random

# Creates a random word from the system dictionary
# USAGE: python random_word.py
# Does not take any arguments

word_file = "/usr/share/dict/words"

WORDS = open(word_file).read().splitlines()

# for i in WORDS:
#     print(i)

for i in range(1):
    l = ''.join(WORDS[random.randint(1, len(WORDS))])
    print(l)
