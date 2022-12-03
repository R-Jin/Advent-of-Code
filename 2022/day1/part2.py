#!/usr/bin/env python3

# --------------------- Part 2 ---------------------
# Reading each of the lines in the text file into the list
lines = []
with open('input') as f:
    lines = f.readlines()

highest = 0
second = 0
third = 0
sum = 0

for number in lines:
    # Newline means end of the group
    if number == '\n':
        # If sum of group higher than previous highest sum
        # Update highest, second and third.
        if highest < sum:
            third = second
            second = highest
            highest = sum
        # Same idea as above
        elif second < sum:
            third = second
            second = sum
        elif third < sum:
            third = sum

        sum = 0
    else:
        sum += int(number)

print(highest + second + third)
