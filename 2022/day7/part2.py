#!/usr/bin/env python3

# --------------------- Part 2 ---------------------
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

folder_sizes = []

for row in lines:
    row = row.split(" ")

    if (row[1] == "cd"):
        if (row[2] == '..\n'):
            dir_size = files_sum
            if cd_back:
            # Pop the nodes size from size_stack
                dir_size = size_stack.pop()

            folder_sizes.append(dir_size)
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

    folder_sizes.append(dir_size)

    # Check if dir size is
    if dir_size <= limit:
        ans += dir_size

    # Add this size into the parent node
    size_stack[-1] += dir_size

    cd_back = True

root_size = size_stack.pop()

disk_size = 70000000
update_size = 30000000
available_size = disk_size - root_size
lowest_deletion_size = update_size - available_size

folder_sizes.sort()

def binary_search(size):
    lo = 0
    hi = len(folder_sizes) - 1

    smallest_mid = 0

    while lo <= hi:
        mid = (lo + hi) // 2
        if folder_sizes[mid] > size:
            smallest_mid = mid
            hi = mid - 1
        elif folder_sizes[mid] < size:
            lo = mid + 1
        else:
            return mid

    return smallest_mid

index = binary_search(lowest_deletion_size)

print(folder_sizes[index])
