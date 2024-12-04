import sys
import numpy as np

with open(sys.argv[1], 'r') as file:
    matrix = np.array([list(line.strip()) for line in file])

def part1_count(matrix, i, j):
    x_axis, y_axis, linear, negative_linear = '', '', '', ''
    
    if(j+3 < matrix.shape[1]):
        x_axis = matrix[i,j] + matrix[i,j+1] + matrix[i,j+2] + matrix[i,j+3]
    if(i+3 < matrix.shape[0]):
        y_axis = matrix[i,j] + matrix[i+1,j] + matrix[i+2,j] + matrix[i+3,j]
    if(i+3 < matrix.shape[0] and j-3>=0):
        linear = matrix[i,j] + matrix[i+1,j-1] + matrix[i+2,j-2] + matrix[i+3,j-3] 
    if(i+3 < matrix.shape[0] and j+3 < matrix.shape[1]):
        negative_linear = matrix[i,j] + matrix[i+1,j+1] + matrix[i+2,j+2] + matrix[i+3,j+3]
    
    return sum([1 for word in [x_axis, y_axis, linear, negative_linear] if word=='XMAS' or word=='SAMX'])

part1 = 0

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        part1 += part1_count(matrix, i, j)

print(f'Part 1: {part1}')


def part2_count(matrix, i, j):    
    linear = matrix[i+1,j-1] + matrix[i,j] + matrix[i-1,j+1]
    negative_linear = matrix[i-1,j-1] + matrix[i,j] + matrix[i+1,j+1] 

    return 1 if all([word in ['MAS', 'SAM'] for word in [linear,negative_linear]]) else 0

part2 = 0

for i in range(1,matrix.shape[0]-1):
    for j in range(1,matrix.shape[1]-1):
        part2 += part2_count(matrix, i, j)

print(f'Part 2: {part2}')