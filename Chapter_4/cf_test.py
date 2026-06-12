#!/usr/bin/env python3

import sys
import unicodedata

START, END = ord(' '), sys.maxunicode + 1

def test_find(*query_words, start=START, end=END):
    print(f"query_words {query_words}")
    query = {w.upper() for w in query_words} #creates a set
    print(query)

test_find('test', 'apple', 'banana', 'banana')