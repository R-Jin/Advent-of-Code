#!/usr/bin/env python3
lines = []
with open('input') as f:
    lines = f.readlines()


hi = 0
s = 0

for number in lines:
    if number == '\n':
        if hi < s:
            hi = s
        s = 0
    else:
        s += int(number)

print(hi)
