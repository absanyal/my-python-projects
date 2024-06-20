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
        
        self.__isadsorped = False
        
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
        self.__isadsorped = False
        
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
    
    def __roll_for_adsorption(self):
        r = np.random.uniform()
        if r < self.__wall.adsorption_p:
            return True
        else:
            return False
        
    
    def step(self):
        dx = np.sqrt(2 * self.Dx * self.dt) * np.random.normal()
        dy = np.sqrt(2 * self.Dy * self.dt) * np.random.normal()
        dz = np.sqrt(2 * self.Dz * self.dt) * np.random.normal()
        
        proposed_x = self.__x + dx
        proposed_y = self.__y + dy
        proposed_z = self.__z + dz
        
        x_inside = 0
        y_inside = 0
        z_inside = 0
        
        full_inside = x_inside * y_inside * z_inside
        adsorped = 0
        
        if self.__wall is not None:
            while not full_inside and not adsorped:
                if proposed_x < self.__xmin or proposed_x > self.__xmax:
                    adsorped = self.__roll_for_adsorption()
                    if adsorped:
                        self.__isadsorped = True
                        break
                    else:
                        dx = np.sqrt(2 * self.Dx * self.dt) * np.random.normal()
                        proposed_x = self.__x + dx
                else:
                    x_inside = 1
                
                if proposed_y < self.__ymin or proposed_y > self.__ymax:
                    adsorped = self.__roll_for_adsorption()
                    if adsorped:
                        self.__isadsorped = True
                        break
                    else:
                        dy = np.sqrt(2 * self.Dy * self.dt) * np.random.normal()
                        proposed_y = self.__y + dy
                else:
                    y_inside = 1
                
                if proposed_z < self.__zmin or proposed_z > self.__zmax:
                    adsorped = self.__roll_for_adsorption()
                    if adsorped:
                        self.__isadsorped = True
                        break
                    else:
                        dz = np.sqrt(2 * self.Dz * self.dt) * np.random.normal()
                        proposed_z = self.__z + dz
                else:
                    z_inside = 1
                
                full_inside = x_inside * y_inside * z_inside
        
        self.__x = proposed_x
        self.__y = proposed_y
        self.__z = proposed_z
        

    @property
    def isadsorped(self):
        return self.__isadsorped
            
        