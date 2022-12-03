#!/usr/bin/env python3

lines = []
with open('test_input') as f:
    lines = f.readlines()

priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

sum = 0

def get_common_item_type(str1, str2):
    for c in str1:
        if c in str2:
            return c

for rucksack in lines:
    n_items = len(rucksack)
    mid = n_items // 2
    compartment1 = rucksack[:mid]
    compartment2 = rucksack[mid:]

    common_item = get_common_item_type(compartment1, compartment2)
    sum += priority.index(common_item) + 1

print(sum)
