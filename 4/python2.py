import sys
import re
import math

file = open(sys.argv[1], "r")

pattern = r"(?P<n>\d+): (?P<winning>.*) \| (?P<playing>.*)$"

og_cards_matches = []
copies = []

for line in file:
    match = re.search(pattern, line)
    winning_numbers = set([int(x) for x in match.group('winning').split()])
    playing_numbers = set([int(x) for x in match.group('playing').split()])

    won_numbers = playing_numbers.intersection(winning_numbers)
    og_cards_matches.append(len(won_numbers))
    copies.append(1)

for i in range(len(copies)):
    for j in range(1,og_cards_matches[i]+1):
        if len(copies) > i+j:
            copies[i+j] += copies[i]


print(sum(copies))