f = open('input', 'r')

lines = f.readlines()

f.close()

reports = [list(map(lambda level: int(level), line.split())) for line in lines]

def check_report(report):
    last = report[0]
    increasing = last < report[1]

    if increasing:
        bound = (1, 3)
    else:
        bound = (-3, -1)

    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if not (diff >= bound[0] and diff <= bound[1]):
            return 0
    return 1

s = 0

for report in reports:
    s += check_report(report)

print(s)
