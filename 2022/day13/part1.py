#!/usr/bin/env python3

import json

# --------------------- Part 1 ---------------------
def compare(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return 1
        elif left > right:
            return -1
        else:
            return 0

    elif not type(left) == int and not type(right) == int:
        # Both are lists
        for l_val, r_val in zip(left, right):
            val = compare(l_val, r_val)
            if val:
                # Return if the values does not equal
                return val

        diff = len(left) - len(right)
        if diff == 0:
            return 0
        elif diff > 0:
            return -1
        else:
            return 1
    else:
        # If exactly one value is a list
        if type(left) == int:
            left = [left]
        if type(right) == int:
            right = [right]

        return compare(left, right)



def main():
    # Reading each of the lines in the text file into the list
    lines = []
    with open('input') as f:
        lines = f.read()

    sum = 0

    for i, pair in enumerate(lines.split("\n\n"), start=1):
        pair = pair.split()
        # Turn strings to lists
        packets1, packets2 = json.loads(pair[0]), json.loads(pair[1])
        if compare(packets1, packets2) > 0:
            sum += i

    print(sum)

main()
