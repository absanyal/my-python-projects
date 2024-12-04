import numpy as np
import matplotlib.pyplot as plt
import rcparams
import itertools
from math import comb

def generate_combinations(n, N):
    array = [0] * N
    indices = list(itertools.combinations(range(N), n))
    combinations = []
    for index_set in indices:
        temp_array = array[:]
        for index in index_set:
            temp_array[index] = 1
        combinations.append(temp_array)
    return combinations

def has_b_consecutive_ones(combination, b):
    count = 0
    for bit in combination:
        if bit == 1:
            count += 1
            if count >= b:
                return True
        else:
            count = 0
    return False

N = 20
n_list = np.arange(0, N + 1)

p_matrix = np.zeros((N+1, N+1))

plt.figure(figsize=(8, 6))

for n in n_list:
    print("Calculating for n = ", n)
    for b in range(0, n + 1):
        combinations = generate_combinations(n, N)
        count = 0
        for combination in combinations:
            if has_b_consecutive_ones(combination, b):
                count += 1
        p_matrix[n, b] = count / comb(N, n)
        
plt.clf()

plt.imshow(p_matrix, cmap='binary', vmin=0, vmax=1, origin='lower', interpolation='quadric')

plt.xlabel(r'$b$')
plt.ylabel(r'$n$')

plt.title(r'$N = {}$'.format(N))

plt.colorbar()

plt.savefig('p_matrix.pdf')
