import numpy as np
from modules.wall import wall

class walker:
    def __init__(self, D, x0, y0, z0, dt, wall: wall = None):
        self.__D = D
        self.__x = x0
        self.__y = y0
        self.__z = z0
        self.__wall = wall
        
        self.__x0 = x0
        self.__y0 = y0
        self.__z0 = z0
        
        if wall is not None:
            self.__xmin = wall.xmin
            self.__xmax = wall.xmax
            self.__ymin = wall.ymin
            self.__ymax = wall.ymax
            self.__zmin = wall.zmin
            self.__zmax = wall.zmax
        self.__dt = dt
        self.position = np.array([self.__x, self.__y, self.__z])
    
    def reset(self):
        self.__x = self.__x0
        self.__y = self.__y0
        self.__z = self.__z0
        
    @property
    def D(self):
        return self.__D
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def z(self):
        return self.__z
    
    @property
    def Dx(self):
        return self.__D[0]
    
    @property
    def Dy(self):
        return self.__D[1]
    
    @property
    def Dz(self):
        return self.__D[2]
    
    @property
    def dt(self):
        return self.__dt
    
    def check_collision(self):
        if self.__x < self.__xmin:
            self.__x = self.__xmin
        if self.__x > self.__xmax:
            self.__x = self.__xmax
        if self.__y < self.__ymin:
            self.__y = self.__ymin
        if self.__y > self.__ymax:
            self.__y = self.__ymax
        if self.__z < self.__zmin:
            self.__z = self.__zmin
        if self.__z > self.__zmax:
            self.__z = self.__zmax
    
    def step(self):
        dx = np.sqrt(2 * self.Dx * self.dt) * np.random.normal()
        dy = np.sqrt(2 * self.Dy * self.dt) * np.random.normal()
        dz = np.sqrt(2 * self.Dz * self.dt) * np.random.normal()
        
        self.__x += dx
        self.__y += dy
        self.__z += dz
        
        if self.__wall is not None:
            self.check_collision()
        