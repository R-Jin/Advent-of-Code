#!/usr/bin/env python3

# --------------------- Part 1 ---------------------
# Reading each of the lines in the text file into the list
lines = []
with open('input') as f:
    lines = f.readlines()

def fully_contains(section1, section2) -> bool:
    """
    If one section is fully contained in the other
    return true
    otherwise false
    """
    section1 = section1.split('-')
    section2 = section2.split('-')

    # Section 2 is fully contained in Section 1
    if int(section1[0]) <= int(section2[0]) and int(section1[1]) >= int(section2[1]):
        return True
    # Section 1 is fully contained in Section 2
    elif int(section2[0]) <= int(section1[0]) and int(section2[1]) >= int(section1[1]):
        return True
    else:
        return False

num = 0

for row in lines:
    pair = row[:-1].split(',')

    if (fully_contains(pair[0], pair[1])):
        num += 1

print(num)
