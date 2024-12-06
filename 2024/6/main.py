import sys
import numpy as np

m_str = ''

from enum import Enum

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

with open(sys.argv[1]) as file:
    m_str = file.read().rstrip()

def parse_map_str(m_str):
    rows = []
    direction = Direction.UP
    for line in m_str.split('\n'):
        row = []
        for c in line:
            i = 2
            match c:
                case '.':
                    i = 0
                case '#':
                    i = -1
                case 'X':
                    i = 1
                case '^':
                    direction = Direction.UP
                case '>':
                    direction = Direction.RIGHT
                case 'v':
                    direction = Direction.DOWN
                case '<':
                    direction = Direction.LEFT
            row.append(i)
        rows.append(row)
    return np.array(rows), direction

m, direction = parse_map_str(m_str)
i,j = [x[0] for x in np.where(m==2)]

out_of_bound = lambda m, i, j: m.shape[0] <= i or i < 0 or m.shape[1] <= j or j < 0

def steps(m, direction, i, j):
    previous = (i,j)
    m[i,j] = 1
    match direction:
        case Direction.UP:
            i-=1
            new_direction = Direction.RIGHT
        case Direction.RIGHT:
            j+=1
            new_direction = Direction.DOWN
        case Direction.DOWN:
            i+=1
            new_direction = Direction.LEFT
        case Direction.LEFT:
            j-=1
            new_direction = Direction.UP
    if out_of_bound(m, i, j):
        return m
    
    if m[i,j] == -1:
        i, j = previous
        return steps(m, new_direction, i, j)
    
    return steps(m, direction, i, j)

clean_m = lambda x: max(x, 0)
v_clean_m = np.vectorize(clean_m)

sys.setrecursionlimit(10000)

result_m = steps(m, direction, i, j)

part1 = v_clean_m(result_m).sum()

print(f'Part 1: {part1}')