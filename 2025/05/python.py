def parse_input(filename):
    ranges = []
    items = []
    
    with open(filename) as file:
        lines = file.read().strip().split('\n\n')
        
        for line in lines[0].split('\n'):
            a, b = line.split('-')
            ranges.append((int(a), int(b)))
        
        for line in lines[1].split('\n'):
            items.append(int(line))
    
    return ranges, items


def is_in_range(value, range_tuple):
    a, b = range_tuple
    return a <= value <= b


def merge_ranges(ranges):
    ranges.sort()
    merged = []
    
    i = 0
    while i < len(ranges):
        start, end = ranges[i]
        
        while i + 1 < len(ranges):
            next_start, next_end = ranges[i + 1]
            if end >= next_start:
                end = max(end, next_end)
                i += 1
            else:
                break
        
        merged.append((start, end))
        i += 1
    
    return merged


def count_fresh_items(ranges, items):
    count = 0
    for item in items:
        if any(is_in_range(item, r) for r in ranges):
            count += 1
    return count


def count_total_in_ranges(ranges):
    return sum(end - start + 1 for start, end in ranges)

ranges, items = parse_input("input.txt")

part1 = count_fresh_items(ranges, items)
print(f'Part 1: {part1}')

part2 = count_total_in_ranges(merge_ranges(ranges))
print(f'Part 2: {part2}')