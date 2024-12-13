import sys
import re
import numpy as np
from math import isclose

eq_re = 'Button (A|B): X\+(\d+), Y\+(\d+)'
sol_re = 'Prize: X=(\d+), Y=(\d+)'

with open(sys.argv[1]) as file:
    all_text = file.read()

def text_to_system(system_str, isPart1):
    eq1_str, eq2_str, sol_str = system_str.split('\n')
    _, a0, b0 = re.match(eq_re, eq1_str).groups()
    _, a1, b1 = re.match(eq_re, eq2_str).groups()
    a_sol, b_sol = re.match(sol_re, sol_str).groups()
    
    eqs = np.array([[a0, a1],[b0, b1]], dtype=int)
    sol = np.array([a_sol, b_sol], dtype=int)
    
    return eqs, sol if isPart1 else sol + np.array([10000000000000, 10000000000000])
    
def solve_cost(system):
    eqs, sol = system
    a, b = np.linalg.solve(eqs, sol)
    if a >=0 and b >= 0 and isclose(a, round(a), rel_tol=1e-15, abs_tol=0.0) and isclose(b, round(b), rel_tol=1e-12, abs_tol=0.0):
        return 3*a + b
    else: 
        return 0

part1 = sum([solve_cost(text_to_system(system_str, True)) for system_str in all_text.split('\n\n')])
print(f'Part 1: {part1}')

part2 = sum([solve_cost(text_to_system(system_str, False)) for system_str in all_text.split('\n\n')])
print(f'Part 2: {part2}')