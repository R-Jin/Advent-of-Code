#!/usr/bin/env python3

# --------------------- Part 2 ---------------------
# Reading each of the lines in the text file into the list
lines = []
with open('input') as f:
    lines = f.readlines()

visited = set()

head_pos = (0, 0)
tail_pos = (0, 0)

knots = [(0, 0) for _ in range(10)]

def move_tail(head_pos, tail_pos):
    dx, dy = head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1]

    if (abs(dx) > 1 or abs(dy) > 1):
        if abs(dx) > 1:
            dx /= abs(dx)

        if abs(dy) > 1:
            dy /= abs(dy)

        tail_pos = (tail_pos[0] + dx, tail_pos[1] + dy)

    return tail_pos

def move_head(direction, head):
    if direction == 'U':
        head = (head[0], head[1] + 1)
    elif direction == 'D':
        head = (head[0], head[1] - 1)
    elif direction == 'L':
        head = (head[0] - 1, head[1])
    elif direction == 'R':
        head = (head[0] + 1, head[1])

    return head

for moves in lines:
    moves = moves.split()
    direction = moves[0]
    steps = int(moves[1])

    for _ in range(steps):
        knots[0] = move_head(direction, knots[0])
        for j in range(1, len(knots)):
            knots[j] = move_tail(knots[j - 1], knots[j])

        visited.add(knots[-1])
print(len(visited))
