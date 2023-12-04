import sys
import re
import math

file = open(sys.argv[1], "r")

all_str = file.read()

seeds = [int(x) for x in all_str.split("\n")[0].split(':')[1].split() if x!=""]

map_strs = [x.split(':')[1] for x in all_str.split("\n\n")[1:]]

def map_str_to_map(map_str):
    map_dic = []
    lines = [x for x in map_str.split("\n") if x!=""]
    for line in lines:
        dest, source, rang = [int(x) for x in line.split()]
        map_dic.append([dest, source, rang])
    return map_dic

def use_map(key, map_dic):
    for line in map_dic:
        dest, source, rang = line
        if (source <= key) and (source + rang > key):
            return dest + (key - source)
    return key


map_dics = [map_str_to_map(x) for x in map_strs]
seed_locs = [x for x in seeds]


for i in range(len(seeds)):
    temp_seed = seeds[i]
    for m in map_dics:
        temp_seed = use_map(temp_seed,m)
    seed_locs[i] = temp_seed

print(min(seed_locs))