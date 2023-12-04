import sys
import re
import math

file = open(sys.argv[1], "r")

all_str = file.read()

seeds = [int(x) for x in all_str.split("\n")[0].split(':')[1].split() if x!=""]
seed_ranges = []

for i in range(len(seeds)):
    if (i % 2) == 0:
        seed_ranges.append([seeds[i],seeds[i+1]])

map_strs = [x.split(':')[1] for x in all_str.split("\n\n")[1:]]

def map_str_to_map(map_str):
    map_dic = []
    lines = [x for x in map_str.split("\n") if x!=""]
    for line in lines:
        dest, source, rang = [int(x) for x in line.split()]
        map_dic.append([dest, source, rang])
    return map_dic

map_dics = [map_str_to_map(x) for x in map_strs]
seed_locs = [x for x in seeds]

def use_map(seed_range, map_dic):
    all_done = False
    seed_key, seed_rang = seed_range
    for line in map_dic:
        dest, source, rang = line
        if seed_key in range(source, source+rang):
            if seed_key + seed_rang in range(source, source+rang):
                return [[dest + (seed_key - source), seed_rang]]
            else:
                #in
                n_in = (source + rang) - seed_key
                return [[dest + (seed_key - source), n_in]] + use_map((seed_key + n_in, seed_rang - n_in), map_dic)
                
    return [[seed_key, seed_rang]]


for m in map_dics:
    temp = []
    for seed_range in seed_ranges:
        temp+=(use_map(seed_range,m))
    seed_ranges = temp

print(min([x[0] for x in seed_ranges]))

