import sys
import numpy as np


reports = []

with open(sys.argv[1]) as file:
    for line in file:
        reports.append(list(map(int,line.split())))

def safe(report):
    head, *tail = report
    return _safe(head, tail[0] - head, tail)

def _safe(last, change, rest):
    head, *tail = rest
    if(change * (head - last) > 0): # same direction of change
        change = head - last
        if(abs(change) in [1,2,3]):
            if len(tail) == 0:
                return 1
            else:
                return _safe(head, change, tail)
    return 0

part1 = sum([safe(report) for report in reports])
print(f'Part 1: {part1}')    

all_options = lambda report: [report[:i] + report[i+1:] for i in range(len(report))]

part2 = len([1 for report in reports if sum([safe(option) for option in all_options(report)])])
print(f'Part 2: {part2}')
