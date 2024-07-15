import numpy as np

class coin:
    def __init__(self, p_heads):
        self.__p_heads = p_heads
        self.__p_tails = 1 - p_heads
        self.__times_flipped = 0
    
    def flip(self):
        self.__times_flipped += 1
        r = np.random.choice(['H', 'T'], p=[self.__p_heads, self.__p_tails])
        return r
    
    def get_times_flipped(self):
        return self.__times_flipped
    
    def reset(self):
        self.__times_flipped = 0
    
    def set_p_heads(self, p_heads):
        self.__p_heads = p_heads
        self.__p_tails = 1 - p_heads