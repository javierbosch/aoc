import sys
import itertools

def possible_check(total, values, valid_operators):
    for operators in itertools.product(valid_operators, repeat=len(values)-1):
        if valid(total, values, operators):
            return True
    return False

def valid(total, values, operators):
    curr = values[0]
    for i in range(0, len(operators)):
        match operators[i]:
            case '+':
                curr = curr + values[i+1]
            case '*':
                curr = curr * values[i+1]
            case '||':
                curr = int(str(curr) + str(values[i+1]))
    return total == curr


equations = []

with open(sys.argv[1]) as file:
    for line in file:
        total, values_str = line.split(':')
        equations.append((int(total), [int(value) for value in values_str.strip().split(' ')]))

part1 = sum([total for total, values in equations if possible_check(total, values, ['+', '*'])])
print(f'Part 1: {part1}')
    
part2 = sum([total for total, values in equations if possible_check(total, values, ['+', '*', '||'])])
print(f'Part 2: {part2}')