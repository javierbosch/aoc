import sys
data_file = open(sys.argv[1], "r")
data = data_file.read()
lines = data.split("\n")


def compare1(x, y):
    xy = set(x).intersection(set(y))
    return len(xy) == len(x) or len(xy) == len(y)


def parseLine(line):
    fst, snd = line.split(",")
    x1, x2 = fst.split("-")
    y1, y2 = snd.split("-")
    x = list(range(int(x1), int(x2)+1))
    y = list(range(int(y1), int(y2)+1))
    return x, y


def compare2(x, y):
    xy = set(x).intersection(set(y))
    return len(xy) > 0


t1 = 0
t2 = 0
for line in lines:
    x, y = parseLine(line)
    t1 += compare1(x, y)
    t2 += compare2(x, y)

print("Part 1:", t1)
print("Part 2:", t2)

data_file.close()
