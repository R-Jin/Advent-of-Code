#!/usr/bin/env python3

# --------------------- Part 1 ---------------------
monkeys = {}
inspections = []

def parse_monkey(monkey):
    monkey_id = 0
    starting_items = []

    for attr in monkey.split('\n'):
        # Get monkey id
        if attr[0:6] == 'Monkey':
            monkey_id = int(attr[-2])
            monkeys[monkey_id] = []

        # Get starting items
        elif attr[2: 16] == 'Starting items':
            starting_items = attr[18:].split(', ')

    for item in starting_items:
        monkeys[monkey_id].append(int(item))

def monkey_turn(monkey):
    monkey_id = 0
    operation = []
    test = 0
    true = 0
    false = 0

    for attr in monkey.split('\n'):
        attr = attr.lstrip()
        # Get monkey id
        if attr[:6] == 'Monkey':
            monkey_id = int(attr[-2])

        elif attr[:9] == 'Operation':
            operation = attr[11:].split()

        elif attr[:4] == 'Test':
            test = int(attr.split()[-1])

        elif attr[:7] == 'If true':
            true = int(attr.split()[-1])

        elif attr[:8] == 'If false':
            false = int(attr.split()[-1])

    items = monkeys[monkey_id]
    inspections[monkey_id] += len(items)

    while items:
        item = items.pop(0)
        item = execute_operations(item, operation)
        item //= 3
        if item % test == 0:
            monkeys[true].append(item)
        else:
            monkeys[false].append(item)

def execute_operations(old_value, operation):
    operator = operation[3]
    a = operation[2]
    b = operation[4]

    if a == 'old':
        a = old_value
    else:
        a = int(a)

    if b == 'old':
        b = old_value
    else:
        b = int(b)

    if operator == '+':
        return a + b

    return a * b


def main():
    # Reading each of the lines in the text file into the list
    lines = []
    with open('input') as f:
        lines = f.read()

    for monkey in lines.split("\n\n"):
        inspections.append(0)
        parse_monkey(monkey)


    for _ in range(20):
        for monkey in lines.split("\n\n"):
            monkey_turn(monkey)

    inspections.sort()
    print(inspections[-1] * inspections[-2])

main()
