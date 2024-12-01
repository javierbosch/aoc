import sys

zipped = [line.split() for line in open(sys.argv[1], "r")]

l1, l2 = [list(sorted(map(int, l))) for l in zip(*zipped)]
part1 = sum([max(a - b, b - a) for a,b in zip(l1,l2)])
print(f'Part 1: {part1}')

l2_table = {n:l2.count(n) for n in l2}
part2 = sum([n*l2_table[n] for n in l1 if n in l2])
print(f'Part 2: {part2}')