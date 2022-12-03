#!/usr/bin/env python3

# --------------------- Part 2 ---------------------
# Reading each of the lines in the text file into the list
lines = []
with open('input') as f:
    lines = f.readlines()

priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

sum = 0

def get_common_item_type(str1, str2, str3):
    """Get first common char in str1, str2 and str3"""
    for c in str1:
        if c in str2 and c in str3:
            return c

for i in range(0, len(lines), 3):
    badge = get_common_item_type(lines[i], lines[i + 1], lines[i + 2])
    # Add 1 to sum due to zero indexing
    sum += priority.index(badge) + 1

print(sum)
