#!/usr/bin/env python3

# --------------------- Part 1 ---------------------
# Reading each of the lines in the text file into the list
lines = []
with open('input') as f:
    lines = f.readlines()

# Stack with the size of all the files in each directory excluding dirs
size_stack = []

begin_sum = False
files_sum = 0
limit = 100000
ans = 0
cd_back = False

for row in lines:
    row = row.split(" ")

    if (row[1] == "cd"):
        if (row[2] == '..\n'):
            dir_size = files_sum
            if cd_back:
            # Pop the nodes size from size_stack
                dir_size = size_stack.pop()

            # Check if dir size is
            if dir_size <= limit:
                ans += dir_size
            # Add this size into the parent node
            size_stack[-1] += dir_size
            cd_back = True
        else:
            if not cd_back:
                size_stack.append(files_sum)
            cd_back = False

        files_sum = 0
        begin_sum = False

    elif (row[1] == "ls\n"):
        begin_sum = True

    elif begin_sum and row[0] != "dir":
        files_sum += int(row[0])

# Handle the last elements in the size_stack
while len(size_stack) > 1:
    dir_size = files_sum
    if cd_back:
    # Pop the nodes size from size_stack
        dir_size = size_stack.pop()

    # Check if dir size is
    if dir_size <= limit:
        ans += dir_size

    # Add this size into the parent node
    size_stack[-1] += dir_size

    cd_back = True

root_size = size_stack.pop()

if root_size <= limit:
    ans += root_size

print(ans)
