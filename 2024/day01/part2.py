"""Day 1 part 2"""
f = open('input', 'r')

lines = f.readlines()

f.close()

loc_1 = map(lambda line: int(line.split()[0]), lines)
loc_2 = list(map(lambda line: int(line.split()[1]), lines))

count = {}

sum = 0


def count_id(target):
    sum = 0
    for i in loc_2:
        if target == i:
            sum += 1
    count[target] = sum
    return sum


for id_1 in loc_1:
    if id_1 in count:
        sum += id_1 * count[id_1]
    else:
        sum += id_1 * count_id(id_1)

print(sum)
