"""Day 1 part 1"""
f = open('input', 'r')

lines = f.readlines()

f.close()

loc_1 = sorted(map(lambda line: int(line.split()[0]), lines))
loc_2 = sorted(map(lambda line: int(line.split()[1]), lines))

sum = 0

for pair in zip(loc_1, loc_2):
    sum += abs(pair[0] - pair[1])

print(sum)
