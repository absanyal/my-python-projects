import numpy as np
import matplotlib.pyplot as plt
from sympy import sequence

n_trials = 1000000

n_flips = 100

A_wins = 0
B_wins = 0
draws = 0

for n in range(n_trials):
    
    if (n+1) % 50000 == 0:
        print('Simulation {}/{}'.format(n+1, n_trials))
        
    sequence = np.random.choice(['H', 'T'], size=n_flips)
    
    A_points = 0
    B_points = 0
    
    for i in range(1, len(sequence)):
        if sequence[i-1] == 'T' and sequence[i] == 'H':
            A_points += 1
        # elif sequence[i-1] == 'T' and sequence[i] == 'T':
        #     A_points += 1
        elif sequence[i-1] == 'H' and sequence[i] == 'H':
            B_points += 1
        # elif sequence[i-1] == 'T' and sequence[i] == 'H':
        #     B_points += 1
    
    if A_points > B_points:
        A_wins += 1
    elif B_points > A_points:
        B_wins += 1
    else:
        draws += 1

print('A wins : {:>2.2f}%'.format(A_wins/n_trials*100))
print('B wins : {:>2.2f}%'.format(B_wins/n_trials*100))
print('Draws  : {:>2.2f}%'.format(draws/n_trials*100))