#!/usr/bin/env python3

# --------------------- Part 1 ---------------------
# Reading each of the lines in the text file into the list
lines = []
with open('input') as f:
    lines = f.readlines()

score = 0

for round in lines:
    elf = round[0]
    # -2 since the last char is '\n'
    me = round[-2]

    # If it is a tie
    if (elf == 'A' and me == 'X') or (elf == 'B' and me == 'Y') or (elf == 'C' and me == 'Z'):
        score += 3
    # If we win the round
    elif (elf == 'A' and me == 'Y'):
        score += 6
    elif (elf == 'B' and me == 'Z'):
        score += 6
    elif (elf == 'C' and me == 'X'):
        score += 6
    # If we lose don't add anything

    # Add the score of the chosen shape
    if (me == 'X'):
        score += 1
    elif (me == 'Y'):
        score += 2
    elif (me == 'Z'):
        score += 3

print(score)
