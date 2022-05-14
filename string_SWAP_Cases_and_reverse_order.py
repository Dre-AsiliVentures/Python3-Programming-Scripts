import math
import os
import random
import re
import sys

def reverse_sentences_in_words_order_and_swap_cases(s):
    # Complete this function
    s = s.swapcase()
    s = s[::-1]
    return s
def reverse_words_order_and_swap_cases(sentence):
    # Complete this function
    sentence = sentence.swapcase()
    words = sentence.split( )
    string=[]
    for word in words:
        string.insert(0,word)
    return ' '.join(string)
if __name__ == '__main__':
    s = rawinput()
    result = reverse_sentences_in_words_order_and_swap_cases(s)
    print(result)
    result = reverse_words_order_and_swap_cases(s)
    print(result)