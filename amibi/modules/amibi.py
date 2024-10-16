import numpy as np

class amibi:
    def __init__(self, DNA1, DNA2):
        if len(DNA1) != len(DNA2):
            raise ValueError("DNA1 and DNA2 must be the same length")
        self.__check_validity_of_DNA()
        self.__DNA1 = DNA1
        self.__DNA2 = DNA2
        self.__age = 0
        self.__energy = 100
        self.__alive = True
        self.__directives = self.__translate()
    
    def __check_validity_of_DNA(self):
        s1 = self.__DNA1
        for base in s1:
            if base!=0 or base!=1:
                raise ValueError("DNA bases must be 0 or 1")
        s2 = self.__DNA2
        for base in s2:
            if base!=0 or base!=1:
                raise ValueError("DNA bases must be 0 or 1")
    
    def __translate(self):
        s1 = self.__DNA1
        s2 = self.__DNA2
        directives = []
        for b1, b2 in zip(s1, s2):
            if b1 == 0 and b2 == 0:
                
                
    
    def tick(self):
        self.__age += 1
        

    @property
    def DNA1(self):
        return self.__DNA1
    
    @property
    def DNA2(self):
        return self.__DNA2