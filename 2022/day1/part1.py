#!/usr/bin/env python3

# --------------------- Part 1 ---------------------
# Reading each of the lines in the text file into the list
lines = []
with open('input') as f:
    lines = f.readlines()

highest = 0
sum = 0

for number in lines:
    # Newline means end of the group
    if number == '\n':
        if highest < sum:
            highest = sum
        sum = 0
    else:
        sum += int(number)

print(highest)
