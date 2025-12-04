import numpy as np

sample_m = (np.genfromtxt('sample.txt', dtype='str', delimiter=1) == '@').astype(int)
input_m = (np.genfromtxt('input.txt', dtype='str', delimiter=1) == '@').astype(int)

def step_matrix(count, matrix):
    new_matrix = np.zeros(matrix.shape)
    x_max, y_max = matrix.shape
    
    for i in range(x_max):
        for j in range(y_max):
            if (matrix[i,j] == 1):
                total = matrix[max(0, i - 1):min(x_max, i + 2), max(0, j - 1):min(y_max, j + 2)].sum()
                if total < 5:
                    count += 1
                else:
                    new_matrix[i,j] = 1

    return count, new_matrix
    
def all_steps(count, matrix):    
    new_count, new_matrix = step_matrix(count, matrix)
    return count if new_count == count else all_steps(new_count, new_matrix)
    
assert step_matrix(0, sample_m)[0] == 13
print(f'Part 1: {step_matrix(0, input_m)[0]}')

assert all_steps(0, sample_m) == 43
print(f'Part 2: {all_steps(0, input_m)}')