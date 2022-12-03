#!/usr/bin/env python3

# --------------------- Part 2 ---------------------
# Reading each of the lines in the text file into the list
lines = []
with open('input') as f:
    lines = f.readlines()

score = 0

for round in lines:
    elf = round[0]
    outcome = round[-2]

    # The case where we need to lose
    if (outcome == 'X'):
        if (elf == 'A'):
            score += 3
        elif (elf == 'B'):
            score += 1
        elif (elf == 'C'):
            score += 2

    # The case where we need to end the round in draw
    elif (outcome == 'Y'):
        score += 3
        if (elf == 'A'):
            score += 1
        elif (elf == 'B'):
            score += 2
        elif (elf == 'C'):
            score += 3

    # The case where we need to win
    elif (outcome == 'Z'):
        score += 6
        if (elf == 'A'):
            score += 2
        elif (elf == 'B'):
            score += 3
        elif (elf == 'C'):
            score += 1


print(score)
