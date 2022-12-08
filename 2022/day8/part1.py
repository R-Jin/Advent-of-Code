#!/usr/bin/env python3

# --------------------- Part 1 ---------------------
# Reading each of the lines in the text file into the list
lines = []
with open('input') as f:
    lines = f.readlines()

ans = 0

visible_coordinates = []

largest_top = [-1 for i in range(len(lines[0].strip('\n')))]
largest_bottom = [-1 for i in range(len(lines[0].strip('\n')))]

for r in range(len(lines)):

    largest_left = -1
    largest_right = -1

    row = [int(tree) for tree in lines[r].strip("\n")]

    for i in range(len(row)):
        tree = row[i]
        # Handle view from left
        if tree > largest_left:
            visible_coordinates.append((i, r))
            ans += 1
            largest_left = tree

        # Handle view from top
        if tree > largest_top[i]:
            if not ((i, r) in visible_coordinates):
                ans += 1
                visible_coordinates.append((i, r))
            largest_top[i] = tree


    for i in range(len(row)-1, -1, -1):
        tree = row[i]
        # Handle view from left
        if tree > largest_right:
            if not ((i, r) in visible_coordinates):
                ans += 1
                visible_coordinates.append((i, r))
            largest_right = tree

for r in range(len(lines)-1, -1, -1):
    row = [int(tree) for tree in lines[r].strip("\n")]
    for i in range(len(row)):
        tree = row[i]
        # Handle view from bottom
        if tree > largest_bottom[i]:
            if not ((i, r) in visible_coordinates):
                ans += 1
                visible_coordinates.append((i, r))
            largest_bottom[i] = tree

print(ans)
