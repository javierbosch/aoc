import sys

def add_rule(rule, order_map):
    x, y = rule.split('|')
    if y in order_map:
        order_map[y].add(x)
    else:
        order_map[y] = set([x])

def check_update(update, order_map):
    head, *tail = update
    return(_check_update(head, tail, order_map))
    
def _check_update(curr, update, order_map):
    if curr in order_map:
        not_valid = order_map[curr].intersection(set(update))
        if not_valid:
            return False
    head, *tail = update
    if tail==[]:
        return True
    else:
        return _check_update(head, tail, order_map)


rules, updates = [], []

with open(sys.argv[1]) as file:
    text = file.read()
    rules, updates = (text.split('\n\n'))
    rules = rules.split()
    updates = [update.split(',') for update in updates.split()]

order_map = {}

for rule in rules:
    add_rule(rule, order_map)

part1 = 0
bad_updates = []
for update in updates:
    if check_update(update, order_map):
        part1 += int(update[len(update) // 2])
    else:
        bad_updates.append(update)
print(f'Part 1: {part1}')


def sort_update(update, order_map):
    head, *tail = update
    return _sort_update(head, tail, order_map)
    
def _sort_update(curr, update, order_map):
    if curr in order_map:
        not_valid = order_map[curr].intersection(set(update))
        if not_valid:
            head, *tail = update
            return _sort_update(head, tail + [curr], order_map)
    head, *tail = update
    if tail==[]:
        return [curr, head]
    else:
        return [curr] + _sort_update(head, tail, order_map)

part2 = 0
for update in bad_updates:
    sorted_update = sort_update(update, order_map)
    part2 += int(sorted_update[len(sorted_update) // 2])
print(f'Part 2: {part2}')