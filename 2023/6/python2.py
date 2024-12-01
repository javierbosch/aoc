import sys
from tqdm import tqdm

file = open(sys.argv[1], "r")

lines = file.readlines()
time = int("".join([x for x in lines[0].split(":")[1].split() if x!=""]))
dist = int("".join([x for x in lines[1].split(":")[1].split() if x!=""]))

def options(time, dist):
    count = 0
    for t in tqdm(range(time)):
        spped = t
        remainder = time - t
        if spped * remainder > dist:
            count+=1
    return count

print('b =', options(time, dist))