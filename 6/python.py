import sys

file = open(sys.argv[1], "r")

lines = file.readlines()
times = [int(x) for x in lines[0].split(":")[1].split() if x!=""]
dists = [int(x) for x in lines[1].split(":")[1].split() if x!=""]

def options(time, dist):
    count = 0
    for t in range(time):
        spped = t
        remainder = time - t
        if spped * remainder > dist:
            count+=1
    return count

t = 1
for i in range(len(times)):
    t = t * options(times[i], dists[i])

print('a =',t)