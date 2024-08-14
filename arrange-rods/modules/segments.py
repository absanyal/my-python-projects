import numpy as np

class segment:
    def __init__(self, start_x, start_y, end_x, end_y):
        self.__start_x = start_x
        self.__start_y = start_y
        self.__end_x = end_x
        self.__end_y = end_y
    
    @property
    def start_x(self):
        return self.__start_x
    
    @property
    def start_y(self):
        return self.__start_y
    
    @property
    def end_x(self):
        return self.__end_x
    
    @property
    def end_y(self):
        return self.__end_y
    
    @property
    def start(self):
        return (self.__start_x, self.__start_y)
    
    @property
    def end(self):
        return (self.__end_x, self.__end_y)
    
    @property
    def length(self):
        return np.sqrt((self.__end_x - self.__start_x)**2 + (self.__end_y - self.__start_y)**2)

def check_intersection(s1: segment, s2: segment):
    # check if the two segments intersect
    # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    x1, y1 = s1.start
    x2, y2 = s1.end
    x3, y3 = s2.start
    x4, y4 = s2.end
    
    denominator = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
    if denominator == 0:
        return False
    
    t = ((x1 - x3)*(y3 - y4) - (y1 - y3)*(x3 - x4)) / denominator
    u = -((x1 - x2)*(y1 - y3) - (y1 - y2)*(x1 - x3)) / denominator
    
    if t >= 0 and t <= 1 and u >= 0 and u <= 1:
        return True
    else:
        return False