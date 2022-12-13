#!/usr/bin/env python3

# --------------------- Part 2 ---------------------
# Do search starting from E until we find a or S
def to_matrix(lines):
    maze = []
    for row in lines:
        maze.append(list(row.strip('\n')))

    return maze

def get_starting_node(matrix):
    for r in range((len(matrix))):
        for c in range((len(matrix[0]))):
            if matrix[r][c] == "E":
                return (r, c)

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

rq, cq = [], []
nodes_left_in_layer = 1
nodes_in_next_layer = 0
visited = set()

def explore_neighbours(m, r, c, R, C):
    global nodes_in_next_layer
    node = m[r][c]
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if rr < 0 or cc < 0:
            continue
        if rr >= R or cc >= C:
            continue
        if (rr, cc) in visited:
            continue

        neighbour = m[rr][cc]

        if (neighbour == 'a' and node != 'b') or (neighbour == 'S' and node != 'b'):
            continue

        if node == 'E':
            node = 'z'

        if ord(node) - ord(neighbour) <= 1:
            rq.append(rr)
            cq.append(cc)
            visited.add((rr, cc))
            nodes_in_next_layer += 1

def solve(matrix, start_node):
    R, C = len(matrix), len(matrix[0])
    move_count = 0
    reached_end = False
    rq.append(start_node[0])
    cq.append(start_node[1])
    visited.add(start_node)
    global nodes_left_in_layer, nodes_in_next_layer

    while len(rq) > 0 or len(cq) > 0:
        r = rq.pop(0)
        c = cq.pop(0)
        if matrix[r][c] == "a" or matrix[r][c] == "S":
            reached_end = True
            break
        explore_neighbours(matrix, r, c, R, C)
        nodes_left_in_layer -= 1
        if not nodes_left_in_layer:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1

    if reached_end:
        return move_count
    else:
        return -1

def main():
    # Reading each of the lines in the text file into the list
    lines = []
    with open('input') as f:
        lines = f.readlines()

    matrix = to_matrix(lines)
    start_node = get_starting_node(matrix)
    print(solve(matrix, start_node))

main()
