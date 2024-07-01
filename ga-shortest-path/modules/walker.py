import numpy as np


class walker:
    def __init__(self, x0, y0, path):
        self.__x = x0
        self.__y = y0
        self.__x0 = x0
        self.__y0 = y0
        self.__path = path
        self.__read_pointer = 0
        self.__xpath = [x0]
        self.__ypath = [y0]
        self.__steps_walked = 0

    def read_path(self):
        if self.__read_pointer < len(self.__path):
            current_letter = self.__path[self.__read_pointer]

            angle = current_letter * np.pi * 2

            dx = np.cos(angle)
            dy = np.sin(angle)

            return dx, dy

    def walk(self):
        if self.__read_pointer < len(self.__path):
            dx, dy = self.read_path()
            self.__read_pointer += 1

            self.__x += dx
            self.__y += dy

            self.__xpath.append(self.__x)
            self.__ypath.append(self.__y)

    def reset(self):
        self.__x = self.__x0
        self.__y = self.__y0
        self.__read_pointer = 0
        self.__xpath = [self.__x0]
        self.__ypath = [self.__y0]
        self.__steps_walked = 0

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def xpath(self):
        return self.__xpath

    @property
    def ypath(self):
        return self.__ypath

    @property
    def steps_walked(self):
        return self.__steps_walked

    @property
    def path(self):
        return self.__path

    @property
    def steps_walked(self):
        return len(self.__xpath) - 1


# def breed(walker1: walker, walker2: walker, mutation_rate=0.01, x0=0, y0=0):
#     path1 = walker1.path
#     path2 = walker2.path

#     path = np.zeros(len(path1))

#     num_crossover_points = np.random.randint(0, int(len(path1) / 2))
#     crossover_points = np.random.randint(
#         0, len(path1) - 1, num_crossover_points)
    
#     crossover_points = np.sort(crossover_points)
    
#     crossover_points = np.append(crossover_points, len(path1))
    
#     current_parent = 1
#     current_crossover_point = 0
    
#     for i in range(len(path1)):
#         if i == crossover_points[current_crossover_point]:
#             current_crossover_point += 1
#             current_parent = 1 - current_parent
        
#         if current_parent == 0:
#             path[i] = path1[i]
#         else:
#             path[i] = path2[i]

#     # mutation

#     for i in range(len(path)):
#         r = np.random.rand()
#         if r < mutation_rate:
#             path[i] = path[i] * (1 + np.random.normal(0, 0.1))

#     return walker(x0, y0, path)

def breed(walker1: walker, walker2: walker, mutation_rate=0.01, x0=0, y0=0):
    path1 = walker1.path
    path2 = walker2.path

    path = np.zeros(len(path1))

    for i in range(len(path1)):
        r = np.random.rand()
        if r < 0.5:
            path[i] = path1[i]
        else:
            path[i] = path2[i]
    
    # mutation
    
    for i in range(len(path)):
        r = np.random.rand()
        if r < mutation_rate:
            path[i] = path[i] * (1 + np.random.normal(0, 0.1))
    
    return walker(x0, y0, path)
    
    