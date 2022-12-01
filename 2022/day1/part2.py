#!/usr/bin/env python3
lines = []
with open('input') as f:
    lines = f.readlines()


hi = 0
mid = 0
lo = 0
s = 0

for number in lines:
    if number == '\n':
        if hi < s:
            lo = mid
            mid = hi
            hi = s
        elif mid < s:
            lo = mid
            mid = s
        elif lo < s:
            lo = s

        s = 0
    else:
        s += int(number)

print(hi + mid + lo)
