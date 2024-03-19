import numpy as np
import modules.parameters as prm

class person:
    def __init__(self, age, state = 'S'):
        self.age = age
        self.state = state
    
    def infect(self):
        self.state = 'I'
    
    def recover(self):
        self.state = 'R'
    
    def die(self):
        self.state = 'D'
    
    def susceptible(self):
        self.state = 'S'
    
    def vaccinated(self):
        self.state = 'V'
    
    def update(self):
        self.age += 1
        r = np.random.rand()
        if self.state == 'S':
            if r < prm.S_to_I:
                self.infect()
        elif self.state == 'I':
            if r < prm.I_to_D:
                self.die()
            if r < prm.I_to_R and self.state != 'D':
                self.recover()
        elif self.state == 'R':
            if r < prm.R_to_S:
                self.susceptible()
            if r < prm.R_to_I:
                self.infect()
        elif self.state == 'V':
            v = np.random.rand()
            if v > prm.vaccine_effectiveness:
                self.susceptible()
        r = np.random.rand()
        if r < prm.natural_death_rate and self.age > 0 and self.state != 'D':
            self.die()
