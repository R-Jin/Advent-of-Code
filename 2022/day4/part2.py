#!/usr/bin/env python3

# --------------------- Part 2 ---------------------
# Reading each of the lines in the text file into the list
lines = []
with open('input') as f:
    lines = f.readlines()

def overlaps(section1, section2) -> bool:
    """
    If one section overlaps with the other
    return true
    otherwise false
    """
    section1 = section1.split('-')
    section2 = section2.split('-')

    # Section 1 overlaps with section 2
    if int(section1[0]) >= int(section2[0]) and int(section1[0]) <= int(section2[1]):
        return True
    elif int(section1[1]) >= int(section2[0]) and int(section1[1]) <= int(section2[1]):
        return True

    # Section 2 overlaps with section 1
    elif int(section2[0]) >= int(section1[0]) and int(section2[0]) <= int(section1[1]):
        return True
    elif int(section2[1]) >= int(section1[0]) and int(section2[1]) <= int(section1[1]):
        return True

    # No overlap
    else:
        return False

num = 0

for row in lines:
    pair = row[:-1].split(',')

    if (overlaps(pair[0], pair[1])):
        num += 1

print(num)
