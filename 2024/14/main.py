import sys
import numpy as np
from collections import defaultdict

positions = []
velocities = []

wide = 101
tall = 103

with open(sys.argv[1]) as file:
    for line in file:
        p_str, v_str = line.rstrip().split(' ')
        positions.append(np.array(p_str[2:].split(','), dtype=int))
        velocities.append(np.array(v_str[2:].split(','), dtype=int))
        

def map_mod(p, x_max, y_max):
    x, y = p
    x = x % x_max
    y = y % y_max
    
    return np.array([x, y])

ps = np.array(positions)
vs = np.array(velocities)

ps = ps + (100 * vs)

positions_mod = [map_mod(p, wide, tall) for p in ps]

quadrant_dict = defaultdict(int)
   
def quadrant_count(positions, dict):
    for p in positions:
        x, y = p
        if x < wide//2 and y < tall//2:
            dict['1'] += 1
        if x > wide//2 and y < tall//2:
            dict['2'] += 1
        if x < wide//2 and y > tall//2:
            dict['3'] += 1
        if x > wide//2 and y > tall//2:
            dict['4'] += 1
    return dict


vals = list(quadrant_count(positions_mod,quadrant_dict).values())

part1 = np.prod(vals)

print(f'Part 1: {part1}')