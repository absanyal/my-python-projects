import numpy as np
from modules.wall import wall

class walker:
    def __init__(self, x0, y0, z0, D, dt, wall: wall):
        self.x = x0
        self.y = y0
        self.z = z0
        self.__x0 = x0
        self.__y0 = y0
        self.__z0 = z0
        self.D = D
        self.dt = dt
        self.__wall = wall
    
    def get_init_pos(self):
        return self.__x0, self.__y0, self.__z0
    
    def walk(self):
        dx = np.sqrt(2*self.D[0]*self.dt)*np.random.randn()
        dy = np.sqrt(2*self.D[1]*self.dt)*np.random.randn()
        dz = np.sqrt(2*self.D[2]*self.dt)*np.random.randn()
        self.x += dx
        self.y += dy
        self.z += dz
        in_wall = self.check_bounds(self.__wall)
        if in_wall == 0:
            self.x -= dx
            self.y -= dy
            self.z -= dz
        
    
    def get_pos(self):
        return self.x, self.y, self.z
    
    def reset(self):
        self.x = self.__x0
        self.y = self.__y0
        self.z = self.__z0
    
    def check_bounds(self, wall):
        if wall.x1 <= self.x <= wall.x2 and wall.y1 <= self.y <= wall.y2 and wall.z1 <= self.z <= wall.z2:
            return True
        else:
            return False
    