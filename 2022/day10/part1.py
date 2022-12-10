#!/usr/bin/env python3

# --------------------- Part 1 ---------------------
# Reading each of the lines in the text file into the list

def is_interesting_cycle(cycle):
    return cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220

def execute_instruction(line, cycle, x):
    instruction = line[0]
    value = 0
    if (instruction == 'addx'):
        value = int(line[1])
        for _ in range(2):
            if (is_interesting_cycle(cycle)):
                signal_strengths.append(cycle * x)
            cycle += 1
        x += value

    elif instruction == 'noop':
        if (is_interesting_cycle(cycle)):
            signal_strengths.append(cycle * x)
        cycle += 1

    return (cycle, x)

signal_strengths = []

def main():
    lines = []
    with open('input') as f:
        lines = f.readlines()

    cycle = 1
    x = 1

    for line in lines:
        line = line.split()
        (cycle, x) = execute_instruction(line, cycle, x)

    print(sum(signal_strengths))

main()
