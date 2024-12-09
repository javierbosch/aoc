import sys

disk_map = ''

with open(sys.argv[1]) as file:
    disk_map = [int(n) for n in file.read()]

disk = []

for i, n in enumerate(disk_map):
    disk += [i//2 if i%2==0 else -1 for _ in range(n)]

l = 0
r = len(disk) - 1

while l < r:
    if disk[l] != -1:
        l += 1
    elif disk[r] == -1:
        r -= 1
    else:
        disk[l] = disk[r]
        disk[r] = -1
        l += 1
        r -= 1

checksum = sum(n * i for i, n in enumerate(disk) if n >= 0)

print(f'Part 1: {checksum}')

# HORRIBLE PART 2 ...


disk = [[i//2 if i%2==0 else None for _ in range(n)] if i%2==0 else n for i, n in enumerate(disk_map) if n!= 0]

r = len(disk) - 1

while r >= 0:
    print("%.2f" % (100*(1 - (r/(len(disk)-1)))) + '%')
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

    right_block = disk[r]
    if isinstance(right_block, list):
        l = 0
        while l < r:
            left_block = disk[l]
            if isinstance(left_block, int):
                if left_block >= len(right_block):
                    disk[l] = left_block - len(right_block)
                    disk[r] = len(right_block)
                    disk.insert(l, right_block)
                    r += 1
                    break
            l += 1
    r -= 1
    
i = 0    
checksum = 0

for b in disk:
    if isinstance(b, list):
        for n in b:
            checksum += n * i
            i += 1
    else:
        i += b
        
print(f'Part 2: {checksum}')
    
    