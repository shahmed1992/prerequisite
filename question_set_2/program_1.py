"""
Write a program to compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically.
○	Eg - line = “which is better python 2 or python 3”
○	Output –
"""
from collections import Counter, OrderedDict


class WordFrequency:
    def __init__(self, input_str):
        self.input_str = input_str

    def get_word_frequency(self):
        words = self.input_str.split(" ")
        word_freq = Counter(words)
        word_freq = dict(OrderedDict(sorted(word_freq.items())))
        print(word_freq)

