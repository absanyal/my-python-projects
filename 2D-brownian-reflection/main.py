import numpy as np
import matplotlib.pyplot as plt
import rcparams
from numpy import pi, exp, sqrt, cos, sin
from numpy.random import normal, uniform

def distance(start: np.ndarray[float], end: np.ndarray[float]) -> float:
    """Calculate the distance between two points in 3D space."""
    return np.linalg.norm(start - end)

R = 1.0

n_walkers = 10000

Dx, Dy = 1.0, 1.0

t_steps = 5000
dt = 0.00001
t_list = np.arange(0, t_steps * dt, dt)

x_list = np.zeros((t_steps, n_walkers))
y_list = np.zeros((t_steps, n_walkers))

# Initial position of the walkers
theta0 = uniform(0, 2 * pi)

R_w = 0.99 * R

if R_w <= 0 or R_w >= R:
    raise ValueError("R_w must be between 0 and R")

w_i_x = R_w * cos(theta0)
w_i_y = R_w * sin(theta0)

center = np.array([0, 0])

with open("info.txt", "w") as f:
    f.write("#n_walkers \t Dx \t Dy \t t_steps \t dt \t R \t R_w \t theta0 \t c_x \t c_y\n")
    f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
        n_walkers, Dx, Dy, t_steps, dt, R, R_w, theta0,
        center[0], center[1]))


with open("walker_positions.txt", "w") as f:
    f.write("#t\t")
    for w_i in range(n_walkers):
        f.write("x_{} y_{}\t".format(w_i, w_i))
    f.write("\n")

    for t_i, t in enumerate(t_list):
        
        if (t_i + 1) % 100 == 0 or t_i == t_steps - 1:
            percent_complete = (t_i + 1) / t_steps * 100
            print("Progress: {} / {} steps | {:.2f} %".format(t_i + 1, t_steps, percent_complete))
        
        #Initialize the walkers
        if t_i == 0:
            x_list[t_i, :] = w_i_x
            y_list[t_i, :] = w_i_y
        else:
            x_list[t_i, :] = x_list[t_i - 1, :]
            y_list[t_i, :] = y_list[t_i - 1, :]
            
        for w_i in range(n_walkers):
            
            walker_x = x_list[t_i, w_i]
            walker_y = y_list[t_i, w_i]
            walker_initial = np.array([walker_x, walker_y])
            walker_is_inside = False
            
            while not walker_is_inside:
                dx = sqrt(Dx * dt) * normal()
                dy = sqrt(Dy * dt) * normal()
                
                # Propose a new position for the walker
                proposed_x = walker_x + dx
                proposed_y = walker_y + dy
                proposed_position = np.array([proposed_x, proposed_y])
                
                # Check if the proposed position is inside the circle
                # We use the distance formula to check if the point is inside the circle
                d_proposed = distance(center, proposed_position)
                
                # If the proposed position is inside the circle, accept it
                # Otherwise, reject it and keep the current position of the walker
                # Roll for new proposed position
                if d_proposed < R:
                    x_list[t_i, w_i] = proposed_x
                    y_list[t_i, w_i] = proposed_y
                    walker_is_inside = True
                else:
                    # Roll for new proposed position
                    walker_x = x_list[t_i, w_i]
                    walker_y = y_list[t_i, w_i]
        
        # Write the positions of the walkers to the file
        if (t_i + 1) % 10 == 0 or t_i == t_steps - 1:
            f.write("{}\t".format(t))
            for w_i in range(n_walkers):
                f.write("{} {}\t".format(x_list[t_i, w_i], y_list[t_i, w_i]))
            f.write("\n")
            f.flush()