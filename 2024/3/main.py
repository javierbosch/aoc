import sys
import re

def parse_mul(mul_str):
    a, b = re.findall('\d{1,3}', mul_str)
    return int(a) * int(b)

program = ''
with open(sys.argv[1], 'r') as file:
    program = file.read()

valid_instructions = re.findall('mul\(\d{1,3},\d{1,3}\)', program)
part1 = sum(map(parse_mul, valid_instructions))
print(f'Part 1: {part1}')


valid_instructions = re.findall('(mul\(\d{1,3},\d{1,3}\)|don\'t|do)', program)

part2 = 0
enable_instruction = True

for instruction in valid_instructions:
    match instruction:
        case 'do':
            enable_instruction = True
        case 'don\'t':
            enable_instruction = False
        case _:
            part2 += parse_mul(instruction) if enable_instruction else 0

print(f'Part 2: {part2}')