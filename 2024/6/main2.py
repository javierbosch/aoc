import sys
import numpy as np
from tqdm import tqdm

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

def in_loop(m, direction, i, j, previous_states):
    previous_loc = (i,j)
    
    if previous_loc in previous_states:
        if direction in previous_states[previous_loc]:
            return True
        else:
            previous_states[previous_loc].add(direction)
    else:
        previous_states[previous_loc] = set([direction])
    
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
        return False
    
    if m[i,j] == -1:
        i, j = previous_loc
        return in_loop(m, new_direction, i, j, previous_states)
    
    return in_loop(m, direction, i, j, previous_states)

maps = []

for x in range(m.shape[0]):
    for y in range(m.shape[1]):
        if m[x,y] == 0:
            m_copy = m.copy()
            m_copy[x,y] = -1
            maps.append(m_copy)

results = []

part2 = 0

sys.setrecursionlimit(10000)

for m in tqdm(maps):
    part2 +=  1 if in_loop(m, direction, i, j, {}) else 0

print(f'Part 2: {part2}')