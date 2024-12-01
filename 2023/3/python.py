import sys


 
file = open(sys.argv[1], "r")

lines = [line.strip() for line in file.readlines()]
r_max = len(lines)
c_max = len(lines[0])


def is_symbol(r,c):
    global lines
    char = lines[r][c]
    return not (char.isdigit() or char == '.')

def find_digits(r,c):
    to_check = []
    rs = []
    cs = []
    if r > 0:
        rs.append(-1)
    if c > 0:
        cs.append(-1)
    rs.append(0)
    cs.append(0)
    if c < c_max - 1:
        cs.append(1)
    if r < r_max - 1:
        rs.append(1)

    for i in rs:
        for j in cs:
            to_check.append((r+i,c+j))
    to_check.remove((r,c))
    return to_check

def is_digit(r,c):
    global lines
    return lines[r][c].isdigit()

def are_digits(to_check):
    return [(r,c) for (r,c) in to_check if is_digit(r,c)]

def find_number_range(r,c):
    global lines
    global c_max
    ci = c
    for i in range(c,-1,-1):
        if lines[r][i].isdigit():
            ci = i
        else: 
            break
    
    cj = c
    for j in range(c,c_max):
        if lines[r][j].isdigit():
            cj = j
        else: 
            break

    return (r,(ci,cj))

number_ranges = []

for r in range(0,r_max):
    for c in range(0,c_max):
        if is_symbol(r,c):
            to_check = find_digits(r,c)
            are_digits_list = are_digits(to_check)
            number_ranges += [find_number_range(r,c) for (r,c) in are_digits_list]

def number_range_to_int(number_range):
    global lines
    (r, (c1,c2)) = number_range
    return int(lines[r][c1:c2+1])


unique_number_ranges = list(set(number_ranges))
print(sum([number_range_to_int(x) for x in unique_number_ranges]))

