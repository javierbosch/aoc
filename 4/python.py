import sys
import re
import math

file = open(sys.argv[1], "r")

pattern = r"(?P<n>\d+): (?P<winning>.*) \| (?P<playing>.*)$"

total = 0

for line in file:
    match = re.search(pattern, line)
    winning_numbers = set([int(x) for x in match.group('winning').split()])
    playing_numbers = set([int(x) for x in match.group('playing').split()])

    won_numbers = playing_numbers.intersection(winning_numbers)
    total += math.floor(pow(2,len(won_numbers)-1))

print(total)