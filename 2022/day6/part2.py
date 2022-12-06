#!/usr/bin/env python3
from collections import Counter

# --------------------- Part 2 ---------------------
# Reading each of the lines in the text file into the list
lines = []
with open('input') as f:
    lines = f.readlines()

def dups(str):
    """Check for duplicate char in strings"""

    # Counter(str) returns a dict where the key
    # is the char of the string and value is number
    # of occurences
    for key, val in Counter(str).items():
        # Check to see if there are any duplicates
        if val > 1:
            return True
    return False

row = lines[0]
for i in range(len(row) - 13):
    if not dups(row[i:i+14]):
        print(i + 14)
        break
