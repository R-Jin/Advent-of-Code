#!/usr/bin/env python3
lines = []
with open('input') as f:
    lines = f.readlines()

score = 0
for round in lines:
    elf = round[0]
    me = round[-2]

    if (me == 'X'):
        if (elf == 'A'):
            score += 3
        elif (elf == 'B'):
            score += 1
        elif (elf == 'C'):
            score += 2

    elif (me == 'Y'):
        score += 3
        if (elf == 'A'):
            score += 1
        elif (elf == 'B'):
            score += 2
        elif (elf == 'C'):
            score += 3

    elif (me == 'Z'):
        score += 6
        if (elf == 'A'):
            score += 2
        elif (elf == 'B'):
            score += 3
        elif (elf == 'C'):
            score += 1


print(score)
