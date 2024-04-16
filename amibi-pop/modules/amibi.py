import numpy as np

class amibi:
    def __init__(self, genes):
        self.genes = genes
        self.energy = 100
        self.age = 0
        self.alive = True
    
    def eat(self):
        self.energy += 1
    
    def move(self):
        self.energy -= 1
    
    def age_up(self):
        self.age += 1
    
    def reproduce(self):
        if self.energy > 50 and self.age > 10:
            self.energy -= 50
            gamete = self.genes + np.random.uniform(0, 0.1, 3)
            return amibi(gamete)
    
    def die(self):
        self.alive = False
    
    def decide(self):
        total_weight = sum(self.genes)
        eat_chance = self.genes[0] / total_weight
        move_chance = self.genes[1] / total_weight
        reproduce_chance = self.genes[2] / total_weight
        
        action = np.random.choice(['eat', 'move', 'reproduce'], p=[eat_chance, move_chance, reproduce_chance])
        
        return action