import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, pi

length = 50

lattice_x = np.arange(0, length, 1)
lattice_y = np.arange(0, length, 1)

lattice = np.meshgrid(lattice_x, lattice_y)

plt.figure(tight_layout=True, figsize=(5, 5))

w_x = np.random.randint(0, length)
w_y = np.random.randint(0, length)

t_iters = 1000

wx_history = [w_x]
wy_history = [w_y]

visited_positions = np.zeros((length, length))

visited_positions[w_x, w_y] = 1

total_distance = 0

for t_i in range(t_iters):
    plt.clf()
    plt.plot(lattice[0], lattice[1], 'o', color='black', markersize=0.5)
    visit_success = False
    cornered = False
    tries = 0
    while not visit_success and not cornered:
        tries += 1
        
        dx = np.random.choice([-1, 0, 1])
        if dx == 0:
            dy = np.random.choice([-1, 1])
        else:
            dy = 0
        
        proposed_w_x = w_x + dx
        
        if proposed_w_x < 0:
            proposed_w_x = 0
        elif proposed_w_x >= length:
            proposed_w_x = length - 1
        
        proposed_w_y = w_y + dy
        
        if proposed_w_y < 0:
            proposed_w_y = 0
        elif proposed_w_y >= length:
            proposed_w_y = length - 1
        
        if visited_positions[proposed_w_x, proposed_w_y] == 0:
            w_x = proposed_w_x
            w_y = proposed_w_y
            visit_success = True
            visited_positions[w_x, w_y] = 1
            
            wx_history.append(w_x)
            wy_history.append(w_y)
        
        if np.sum(visited_positions) == length**2:
            cornered = True
        
        if tries > 100:
            cornered = True
            
        if cornered:
            print('Cornered at t = {}'.format(t_i))
        
    if cornered:
        break
    
    
    plt.plot(wx_history, wy_history, '-', color='red', linewidth=0.5)
    
    plt.xticks([])
    plt.yticks([])
    
    plt.savefig('lattice.png')

    
    
    