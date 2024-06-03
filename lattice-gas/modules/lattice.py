import numpy as np

class lattice:
    def __init__(self, Lx, Ly):
        self.sites = np.zeros((Lx, Ly))
    
    def move_occupation(self, source, target):
        source_i, source_j = source[0], source[1]
        target_i, target_j = target[0], target[1]
        
        self.sites[target_i, target_j] = self.sites[source_i, source_j]
        self.sites[source_i, source_j] = 0
    
    def check_nearest_neighbors(self, i, j):
        neighbors = []
        Lx, Ly = self.sites.shape
        
        i_plus_1 = (i + 1) % Lx
        i_minus_1 = (i - 1 + Lx) % Lx
        j_plus_1 = (j + 1) % Ly
        j_minus_1 = (j - 1 + Ly) % Ly
        
        neighbors.append((i_plus_1, j))
        neighbors.append((i_minus_1, j))
        neighbors.append((i, j_plus_1))
        neighbors.append((i, j_minus_1))
        
        return neighbors
    
    def check_free_neighbors(self, i, j):
        neighbors = self.check_nearest_neighbors(i, j)
        free_neighbors = []
        
        for neighbor in neighbors:
            if self.sites[neighbor[0], neighbor[1]] == 0:
                free_neighbors.append(neighbor)
        
        return free_neighbors

    def check_occupied_neighbors(self, i, j):
        neighbors = self.check_nearest_neighbors(i, j)
        occupied_neighbors = []
        
        for neighbor in neighbors:
            if self.sites[neighbor[0], neighbor[1]] != 0:
                occupied_neighbors.append(neighbor)
        
        return occupied_neighbors
    
    def index_to_coordinates(self, index):
        Lx, Ly = self.sites.shape
        i = index // Ly
        j = index % Ly
        
        return i, j
    
    def coordinates_to_index(self, i, j):
        Lx, Ly = self.sites.shape
        index = i * Ly + j
        
        return index
    
    def move_particle(self, i, j):
        free_neighbors = self.check_free_neighbors(i, j)
        
        if len(free_neighbors) > 0:
            target = free_neighbors[np.random.choice(len(free_neighbors))]
            self.move_occupation((i, j), target)
    
    def update(self):
        Lx, Ly = self.sites.shape
        
        for i in range(Lx):
            for j in range(Ly):
                if self.sites[i, j] != 0:
                    self.move_particle(i, j)
    
    def get_num_particles(self):
        return np.sum(self.sites)
    
    