import numpy as np
from numpy import random, sqrt, pi

class rod:
    def __init__(self, initial_angle):
        self.angle = initial_angle
        self.__initial_angle = initial_angle
    
    def rotate(self, theta):
        self.angle += theta
        if self.angle > 2 * pi:
            self.angle -= 2*pi
    
    def get_angle(self):
        return self.angle
    
    def reset(self):
        self.angle = self.__initial_angle