import numpy as np

class pwalker:
    def __init__(self, x0, p_forward, p_backward):
        self.__x = x0
        self.__x0 = x0
        
        if (p_forward + p_backward) > 1:
            print('Error: p_forward + p_backward > 1')
            return
        else:
            self.__p_forward = p_forward
            self.__p_backward = p_backward
            self.__p_stay = 1 - (p_forward + p_backward)
    
    def walk(self):
        r = np.random.rand()
        if r < self.__p_forward:
            self.__x += 1
        elif r < self.__p_forward + self.__p_backward:
            self.__x -= 1
    
    def reset(self):
        self.__x = self.__x0
    
    def get_position(self):
        return self.__x
    
    def get_position0(self):
        return self.__x0
    
    def get_p_forward(self):
        return self.__p_forward
    
    def get_p_backward(self):
        return self.__p_backward
    
    def get_p_stay(self):
        return self.__p_stay
    
    def set_p_forward(self, p_forward):
        self.__p_forward = p_forward
    
    def set_p_backward(self, p_backward):
        self.__p_backward = p_backward
        
    def set_position(self, x):
        self.__x = x
    
    