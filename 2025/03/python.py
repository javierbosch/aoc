import numpy as np

sample_m = np.genfromtxt('sample.txt', delimiter=1)
input_m = np.genfromtxt('input.txt', delimiter=1)

def part1(matrix):
    total = 0
    for row in matrix:
        index_first = row[0:matrix.shape[1]-1].argmax()
        max_second = row[index_first + 1 : matrix.shape[1]].max()
        total += (row[index_first] * 10 + max_second)
    return total

def part2(matrix):
    total = 0
    for row in matrix:
        digits = [int(x) for x in row]
        n = len(digits)
        k = 12  
        to_remove = n - k
        
        stack = []
        for i, digit in enumerate(digits):
            while stack and to_remove > 0 and stack[-1] < digit:
                stack.pop()
                to_remove -= 1
            stack.append(digit)
        
        result = stack[:k]
        
        number = int(''.join(map(str, result)))
        total += number
    return total

assert part1(sample_m) == 357
print(f'Part 1: {part1(input_m)}')

assert part2(sample_m) == 3121910778619
print(f'Part 2: {part2(input_m)}')