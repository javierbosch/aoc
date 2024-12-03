from copy import deepcopy
import sys
data_file = open(sys.argv[1], "r")
data = data_file.read()
lines = data.split("\n")

t1 = 0
stacks = []

def parseLineSetUp(line, stacks):
    for s in range(len(stacks)):
        if line[(s*4)+1] != " ":
            stacks[s].append(line[(s*4)+1])
    return stacks

def parseLineInstruction(line):
    return [int(x) for x in line.split() if x.isnumeric()]

def move(fromStack, toStack, stacks):
    elem = stacks[fromStack-1].pop(0)
    stacks[toStack-1].insert(0,elem)

def moveStacking(amount, fromStack, toStack, stacks):
    elems = stacks[fromStack-1][:amount]
    stacks[fromStack-1] = stacks[fromStack-1][amount:]
    stacks[toStack-1] = elems + stacks[toStack-1] 

stacks = [ [] for _ in range((len(lines[0])+1)//4)]

l = 0
for l in range(len(lines)):
    if lines[l].startswith(' 1'):
        break
    else:
        stacks = parseLineSetUp(lines[l],stacks)
l += 2

stacks_part2 = deepcopy(stacks)


while l < len(lines):
    amount, fromStack, toStack = parseLineInstruction(lines[l])
    for _ in range(amount):
        move(fromStack, toStack, stacks)
    moveStacking(amount,fromStack,toStack,stacks_part2)
    l+=1

print("Part 1:", ''.join([x[0] for x in stacks]))
print("Part 2:", ''.join([x[0] for x in stacks_part2]))

data_file.close()
