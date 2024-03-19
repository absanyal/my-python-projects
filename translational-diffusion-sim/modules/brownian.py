import numpy as np

class particle:
    def __init__(self, x0, y0, z0):
        self.x = x0
        self.y = y0
        self.z = z0
        self.__x0 = x0
        self.__y0 = y0
        self.__z0 = z0
    
    def brownian_move(self, Dx, Dy, Dz, dt):
        self.x += np.sqrt(2 * Dx * dt) * np.random.normal(0, 1)
        self.y += np.sqrt(2 * Dy * dt) *np.random.normal(0, 1)
        self.z += np.sqrt(2 * Dz * dt) *np.random.normal(0, 1)
    
    def reset(self):
        self.x = self.__x0
        self.y = self.__y0
        self.z = self.__z0
    
    def get_position(self):
        return np.array([self.x, self.y, self.z])

def particle_distance(p1, p2):
    return np.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)