import numpy as np

def quadratic_solutions(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return None
    elif d == 0:
        return -b / (2*a)
    else:
        return (-b + np.sqrt(d)) / (2*a), (-b - np.sqrt(d)) / (2*a)

n_data = 1000

parameters_list = []
solutions_list = []

a = 1
for n in range(n_data):
    realsoln = False
    while not realsoln:
        b = np.random.uniform(-100, 100)
        c = np.random.uniform(-100, 100)
        
        if b**2 - 4*a*c >= 0:
            realsoln = True
        
    x1, x2 = quadratic_solutions(a, b, c)
    
    parameters_list.append([a, b, c])
    solutions_list.append([x1, x2])

with open('quadratic_data.txt', 'w') as f:
    f.write("#a\tb\tc\tx1\tx2\n")
    for i in range(n_data):
        f.write("{}\t{}\t{}\t{}\t{}\n".format(parameters_list[i][0], parameters_list[i][1], parameters_list[i][2], solutions_list[i][0], solutions_list[i][1]))