#question 10

from collections import Counter


def countWords(filename):
    with open(filename) as f:
        return Counter(f.read().split())

print("Number of words in the file :",countWords)

