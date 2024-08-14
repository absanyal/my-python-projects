import numpy as np
import matplotlib.pyplot as plt
import rcparams
from modules.segments import segment, check_intersection

canvas_size_x = 10
canvas_size_y = 10
# length = 2

num_rods = 10000
current_segments = []
max_attempts = 100

rods_added = 0

plt.figure(figsize=(canvas_size_x, canvas_size_y))

for rod_i in range(num_rods):
    length = np.random.uniform(0.8, 1.2)
    start_x = np.random.uniform(0, canvas_size_x)
    start_y = np.random.uniform(0, canvas_size_y)
    angle = np.random.uniform(0, 2*np.pi)
    # angle = np.random.uniform(-np.pi/20, np.pi/20)
    end_x = start_x + length*np.cos(angle)
    end_y = start_y + length*np.sin(angle)
       
    
    new_segment = segment(start_x, start_y, end_x, end_y)
    
    attempts = 0
    
    is_intersect = True
    while is_intersect == True and attempts < max_attempts:
        attempts += 1
        is_intersect = False
        for s in current_segments:
            if check_intersection(new_segment, s):
                is_intersect = True
                # angle = np.random.uniform(0, 2*np.pi)
                angle += np.random.uniform(-np.pi/20, np.pi/20)
                end_x = start_x + length*np.cos(angle)
                end_y = start_y + length*np.sin(angle)
                new_segment = segment(start_x, start_y, end_x, end_y)
                break
    
    if is_intersect == False:
        current_segments.append(new_segment)
        rods_added += 1
    
    if rod_i % 1000 == 0:
        print("{} rods added out of {} attempts".format(rods_added, rod_i+1))
    
        plt.clf()
        
        for s in current_segments:
            plt.plot([s.start_x, s.end_x], [s.start_y, s.end_y], 'b')
            
        plt.xlim(0, canvas_size_x)
        plt.ylim(0, canvas_size_y)
        
        plt.gca().set_aspect('equal', adjustable='box')
        
        plt.draw()
        
        plt.savefig("rods.png")