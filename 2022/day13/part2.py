#!/usr/bin/env python3

import json

# --------------------- Part 2 ---------------------
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

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if compare(array[j], pivot) >= 0:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

def quick_sort(array, low, high):
	if low < high:
		pi = partition(array, low, high)
		quick_sort(array, low, pi - 1)
		quick_sort(array, pi + 1, high)

def binary_search(array, key):
    lo = 0
    hi = len(array) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        comp = compare(array[mid], key)
        if comp == 0:
            return mid + 1
        elif comp > 0:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


def main():
    # Reading each of the lines in the text file into the list
    lines = []
    with open('input') as f:
        lines = f.readlines()

    sum = 0

    unsorted = [json.loads(line.strip()) for line in lines if not line == '\n' ]
    unsorted.append([[2]])
    unsorted.append([[6]])

    quick_sort(unsorted, 0, len(unsorted) - 1)

    print(binary_search(unsorted, [[2]]) * binary_search(unsorted, [[6]]))

main()
