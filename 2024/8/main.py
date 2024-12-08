import sys
import itertools
import numpy as np
        
points = {}
max_x, max_y = 0, 0

with open(sys.argv[1]) as file:
    text_lines = [line.strip() for line in file.readlines()]
    for i in range(len(text_lines)):
        for j in range(len(text_lines[i])):
            c = text_lines[i][j] 
            if c != '.':
                if c in points:
                    points[c].append(np.array([i,j]))
                else:
                    points[c] = [np.array([i,j])]
            max_x, max_y = i, j 
            
            
antinodes = lambda p1, p2:  [p1 - (p2 - p1), p2 + (p2 - p1)]
inside = lambda p, max_x, max_y: p[0] >= 0 and p[0] <= max_x and p[1] >= 0 and p[1] <= max_y

all_antinodes = []

for c in points:
    for p1, p2 in itertools.combinations(points[c], 2):
        all_antinodes += antinodes(p1, p2) 

valid_antinodes = [p for p in np.unique(all_antinodes,axis=0) if inside(p, max_x, max_y)]

part1 = len(valid_antinodes)
print(f'Part 1: {part1}')


def antinodes2(p1, p2, max_x, max_y):
    ps = [p1, p2]
    delta = p2 - p1
    while inside(p1 - delta, max_x, max_y):
        ps.append(p1 - delta)
        p1 = p1 - delta
    while inside(p2 + delta, max_x, max_y):
        ps.append(p2 + delta)
        p2 = p2 + delta
    return ps

all_antinodes = []

for c in points:
    for p1, p2 in itertools.combinations(points[c], 2):
        all_antinodes += antinodes2(p1, p2, max_x, max_y) 

valid_antinodes = [p for p in np.unique(all_antinodes,axis=0)]

part2 = len(valid_antinodes)
print(f'Part 2: {part2}')