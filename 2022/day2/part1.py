#!/usr/bin/env python3
lines = []
with open('input') as f:
    lines = f.readlines()

score = 0
for round in lines:
    elf = round[0]
    me = round[-2]

    if (elf == 'A' and me == 'X') or (elf == 'B' and me == 'Y') or (elf == 'C' and me == 'Z'):
        score += 3
    elif (elf == 'A' and me == 'Y'):
        score += 6
    elif (elf == 'B' and me == 'Z'):
        score += 6
    elif (elf == 'C' and me == 'X'):
        score += 6

    if (me == 'X'):
        score += 1
    elif (me == 'Y'):
        score += 2
    elif (me == 'Z'):
        score += 3

print(score)
