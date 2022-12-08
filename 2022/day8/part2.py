#!/usr/bin/env python3

# --------------------- Part 2 ---------------------
# Reading each of the lines in the text file into the list
lines = []
with open('test_input') as f:
    lines = f.readlines()

highest_scenic_score = 0

for r in range(len(lines)):

    row = [int(tree) for tree in lines[r].strip("\n")]

    for i in range(len(row)):
        curr_tree = row[i]
        # Calculate scenic score
        scenic_score = 1

        # Down
        steps = 0
        for y in range(r + 1, len(lines)):
            steps += 1
            if (int(lines[y][i]) >= row[i]):
                break
        scenic_score *= steps

        # Right
        steps = 0
        for x in range(i + 1, len(lines)):
            steps += 1
            if (int(lines[r][x]) >= row[i]):
                break
        scenic_score *= steps

        # Up
        steps = 0
        for y in range(r - 1, -1, -1):
            steps += 1
            if (int(lines[y][i]) >= row[i]):
                break
        scenic_score *= steps


        # Left
        steps = 0
        for x in range(i - 1, -1, -1):
            steps += 1
            if (int(lines[r][x]) >= row[i]):
                break

        scenic_score *= steps
        # print(scenic_score)

        if highest_scenic_score < scenic_score:
            highest_scenic_score = scenic_score

print(highest_scenic_score)
