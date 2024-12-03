import sys
data_file = open(sys.argv[1], "r")
data = data_file.read()
lines = data.split("\n")

def eval(x): return ord(x) - 96 if ord(x) > 96 else ord(x) - 38

# Part 1
t1 = 0
for line in lines:
    fst, snd = set(line[:len(line)//2]), set(line[len(line)//2:])
    u = fst.intersection(snd)
    t1 += eval(u.pop())

# Part 2
t2, i = 0, 0
while i < (len(lines)):
    u = set.intersection(*[set(lines[i+j]) for j in range(3)])
    t2 += eval(u.pop())
    i += 3
    
print(t1,t2)
data_file.close()