import numpy as np
from modules.rod import rod
from numpy import random, sqrt, pi

class brownian_engine:
    def __init__(self, D, dt):
        self.D = D
        self.dt = dt
    
    def perturb(self, rod):
        dtheta = sqrt(2*self.D*self.dt) * random.normal(0, 1)
        rod.rotate(dtheta)
    
    def total_perturb(self, rod, n_iters):
        dtheta_list = sqrt(2*self.D*self.dt) * random.normal(0, 1, n_iters)
        dtheta = np.sum(dtheta_list)
        rod.rotate(dtheta)