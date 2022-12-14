#!/usr/bin/env python3

# --------------------- Part 1 ---------------------
lowest_rock_y = 0
world = set()
sand_start_pos = (500, 0)

def get_rock_pos(row):
    global lowest_rock_y
    coords = [tuple(map(lambda x: int(x),coord.split(','))) for coord in row.split(" -> ")]
    for i in range(1, len(coords)):
        (s_x, s_y) = coords[i - 1]
        (e_x, e_y) = coords[i]
        steps_x = e_x - s_x
        steps_y = e_y - s_y
        if steps_x:
            for j in range(abs(steps_x) + 1):
                dx = steps_x // abs(steps_x)
                y = coords[i - 1][1]
                world.add((coords[i - 1][0] + j * dx, y))
                if y > lowest_rock_y:
                    lowest_rock_y = y

        if steps_y:
            for j in range(abs(steps_y) + 1):
                dy = steps_y // abs(steps_y)
                y = coords[i - 1][1] + j * dy
                world.add((coords[i - 1][0], y))
                if y > lowest_rock_y:
                    lowest_rock_y = y

def sand_in_void():
    """return True if sand falls to void else return False"""
    sand = sand_start_pos
    rest = False
    while not rest:
        if sand[1] > lowest_rock_y:
            return True

        if (sand[0], sand[1] + 1) in world:
            if (sand[0] - 1, sand[1] + 1) in world:
                if (sand[0] + 1, sand[1] + 1) in world:
                    world.add(sand)
                    rest = True
                else:
                    sand = (sand[0] + 1, sand[1] + 1)
            else:
                sand = (sand[0] - 1, sand[1] + 1)
        else:
            sand = (sand[0], sand[1] + 1)

    return False

def main():
    # Reading each of the lines in the text file into the list
    lines = []
    with open('input') as f:
        lines = f.readlines()

    for row in lines:
        row = row.strip()
        get_rock_pos(row)

    in_void = False
    sand_units = 0

    while not in_void:
        in_void = sand_in_void()
        if not in_void:
            sand_units += 1

    print(sand_units)

main()
