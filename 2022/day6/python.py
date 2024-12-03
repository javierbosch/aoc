import sys
data_file = open(sys.argv[1], "r")
data = data_file.read()

for i in range(len(data)):
    s1 = set(data[i:i+4])
    s2 = set(data[i:i+14])
    if len(s1) == 4:
        p1 = i+4
    if len(s2) == 14:
        p2 = i+14
        break

print("Part 1:", p1)
print("Part 2:", p2)

data_file.close()
