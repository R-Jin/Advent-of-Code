#!/usr/bin/env python3

# --------------------- Part 2 ---------------------
painted_row = []
sprite = [0, 1, 2]

def draw_pixel(cycle):
    index = (cycle - 1) % 40
    if index in sprite:
        painted_row.append('#')
    else:
        painted_row.append('.')

def draw_row():
    print("".join(painted_row))

def execute_instruction(line, cycle, x):
    instruction = line[0]
    value = 0
    if (instruction == 'addx'):

        value = int(line[1])

        for _ in range(2):

            draw_pixel(cycle)

            if cycle % 40 == 0:
                draw_row()
                painted_row.clear()

            cycle += 1
        calc_new_sprite(value)

    elif instruction == 'noop':
        draw_pixel(cycle)
        if cycle % 40 == 0:
            draw_row()
            painted_row.clear()
        cycle += 1

    return (cycle, x)


def calc_new_sprite(value):
    sprite[1] += value
    sprite[0] = sprite[1] - 1
    sprite[2] = sprite[1] + 1

def main():
    lines = []
    with open('input') as f:
        lines = f.readlines()

    cycle = 1
    x = 1

    for line in lines:
        line = line.split()
        (cycle, x) = execute_instruction(line, cycle, x)

main()
