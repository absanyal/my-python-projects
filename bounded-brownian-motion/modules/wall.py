import numpy as np

class wall:
    def __init__(self, xmin, xmax, ymin, ymax, zmin, zmax, adsorption_p = 0.0):
        self.__xmin = xmin
        self.__xmax = xmax
        self.__ymin = ymin
        self.__ymax = ymax
        self.__zmin = zmin
        self.__zmax = zmax
        self.__adsorption_p = adsorption_p
    
    @property
    def xmin(self):
        return self.__xmin
    @property
    def xmax(self):
        return self.__xmax
    
    @property
    def xwidth(self):
        return abs(self.__xmax - self.__xmin)
    
    @property
    def ymin(self):
        return self.__ymin
    
    @property
    def ymax(self):
        return self.__ymax
    
    @property
    def ywidth(self):
        return abs(self.__ymax - self.__ymin)
    
    @property
    def zmin(self):
        return self.__zmin
    
    @property
    def zmax(self):
        return self.__zmax
    
    @property
    def zwidth(self):
        return abs(self.__zmax - self.__zmin)
    
    @property
    def adsorption_p(self):
        return self.__adsorption_p