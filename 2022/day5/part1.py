#!/usr/bin/env python3

# --------------------- Part 1 ---------------------
# Reading each of the lines in the text file into the list
lines = []
with open('input') as f:
    lines = f.readlines()

starting_stack_array = lines[:8]        # Get the starting_stack as an array
starting_stack_array.reverse()          # Needs to be reversed for efficient stack structure

starting_stack = {}

def generate_starting_stack():
    """Generate the starting stack from the input"""
    for row in starting_stack_array:
        stack_key = 1
        for i in range(1, len(row), 4):
            # Populate dictionary with [] so
            # that append is immediately available
            if not (stack_key in starting_stack):
                starting_stack[stack_key] = []
            # Add to stack if it is a crate
            if row[i] != ' ':
                starting_stack[stack_key].append(row[i])
            stack_key += 1

def move(n_elem, start, end):
    """Move elements from one stack to another"""
    for _ in range(n_elem):
        starting_stack[end].append(starting_stack[start].pop())

generate_starting_stack()

for i in lines[10:]:
    # Get the instructions
    tmp = i.split(" ")
    n_elem, start, end = int(tmp[1]), int(tmp[3]), int(tmp[5])

    # Move the crate(s)
    move(n_elem, start, end)

res = ""

# Get all the top crates
for key in starting_stack:
    res += starting_stack[key][-1]

print(res)
