import numpy as np
from modules.orthonormal import orthonormal_pair, face_vector
import numpy.linalg as la
from numpy.linalg import norm

class layer:
    def __init__(self, monomer_diameter, start_pos, heading):
        self.__monomer_diameter = monomer_diameter
        self.__start_pos = np.array(start_pos)
        self.__heading = np.array(heading)
        
        self.positions = []
        self.positions.append(self.__start_pos)
        
        self.__generate_layer()
        
    
    def __generate_basis(self):
        h = self.__heading
        h = h / norm(h)
        
        f, g = orthonormal_pair(h)
        
        return h, f, g
    
    def __generate_layer(self):
        h, f, g = self.__generate_basis()
        
        a = self.__monomer_diameter
        
        p0 = self.__start_pos
        p1 = p0 + a * f
        p2 = p0 + a * g
        p3 = p0 + a * (f + g)
        
        self.positions.append(p1)
        self.positions.append(p2)
        self.positions.append(p3)
    
    def make_next_layer(self):
        a = self.__monomer_diameter
        
        start_pos = self.positions[0] + a * (self.__heading / norm(self.__heading))
        
        return layer(self.__monomer_diameter, start_pos, self.__heading)
    
    @property
    def mono_diameter(self):
        return self.__monomer_diameter
        
        
        
        
        
        
        