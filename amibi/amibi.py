import numpy as np
import genetics as g

class amibi:
    def __init__(self, DNA):
        self.age = 0
        self.DNA = DNA
        self.energy = 100
        self.can_reproduce = False
        self.command_queue = []
    
    def age_up(self):
        self.age += 1
        if self.age > 10:
            self.can_reproduce = True
    
    def move(self):
        self.energy -= 1
    
    def eat(self):
        self.energy += 1
    
    
    
    
    
    
        