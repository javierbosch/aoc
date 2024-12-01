import sys
import re

def create_rgb(rgb_str):
    rgb_str = rgb_str.strip()
    n = int("".join([x for x in rgb_str if x.isdigit()]))
    if 'red' in rgb_str:
        return (n,0,0)
    if 'green' in rgb_str:
        return (0,n,0)
    if 'blue' in rgb_str:
        return (0,0,n)

def add_rgbs(rgbs):
    r_t, g_t, b_t = 0, 0, 0
    for rgb in rgbs:
        r,g,b = rgb
        r_t, g_t, b_t = r_t + r, g_t + g, b_t + b
    return (r_t, g_t, b_t)

def max_rgbs(rgbs):
    r_t, g_t, b_t = 0, 0, 0
    for rgb in rgbs:
        r,g,b = rgb
        r_t = r if r > r_t else r_t
        g_t = g if g > g_t else g_t
        b_t = b if b > b_t else b_t
    return (r_t, g_t, b_t)

def rgb1_gt_rgb2(rgb1, rgb2):
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    return (r1 > r2) or (g1 > g2) or (b1 > b2)

file = open(sys.argv[1], "r")

pattern = r"^Game (?P<id>\d+): (?P<sets>.*)$"

total = 0

for line in file:
    match = re.search(pattern, line)
    id_int = int(match.group('id'))
    max_ = max_rgbs([add_rgbs([create_rgb(rgb_str) for rgb_str in set.split(',')]) for set in match.group('sets').split(';')])
    
    r,g,b = max_
    
    total += r * g * b

print(total)







