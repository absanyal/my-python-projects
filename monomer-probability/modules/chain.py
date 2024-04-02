import numpy as np

class chain:
    def __init__(self, chain_length, cost):
        self.chain_length = chain_length
        self.chain = np.zeros(chain_length)
        self.cost = cost
    
    def flip(self, index):
        if self.chain[index] == 0:
            self.chain[index] = 1
        else:
            self.chain[index] = 0
        
    
    def get_connected(self):
        return np.sum(self.chain)

    def get_energy(self):
        return self.cost * self.get_connected()
    
    def randomize(self):
        self.chain = np.random.randint(0, 2, self.chain_length)
    
    def sweep(self, T):
        for i in range(self.chain_length):
            r = np.random.uniform(0, 1)
            old_energy = self.get_energy()
            self.flip(i)
            new_energy = self.get_energy()
            dE = new_energy - old_energy
            boltzmann = np.exp(-dE / T)
            if dE > 0 and r > boltzmann:
                self.flip(i)
            
    
    def get_chain(self):
        return self.chain
    
    def get_chain_length(self):
        return self.chain_length
        

    