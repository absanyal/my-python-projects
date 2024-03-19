from matplotlib import tight_layout
import numpy as np
import matplotlib.pyplot as plt
import modules.parameters as prm
from modules.person import person

population_S = 1000
population_I = 10

t_max = 500

population = []

for i in range(population_S):
    age = int(np.ceil(np.random.normal(40, 10)))
    population.append(person(age, 'S'))
    # print("{} {} {}".format(i, population[i].age, population[i].state))

for i in range(population_I):
    population.append(person(i, 'I'))
    
S_list = np.zeros(t_max)
I_list = np.zeros(t_max)
R_list = np.zeros(t_max)
D_list = np.zeros(t_max)
V_list = np.zeros(t_max)
pop_list = np.zeros(t_max)

for t in range(t_max):
    for p in population:
        
        # Births
        r = np.random.rand()
        if r < prm.natural_birth_rate:
            population.append(person(0, 'S'))
        
        # vaccinate
        
        if p.state == 'S':
            r = np.random.rand()
            if r < prm.vaccine_coverage:
                p.vaccinated()
        
        p.update()
        
        # count all people
        
        if p.state == 'S':
            S_list[t] += 1
        if p.state == 'I':
            I_list[t] += 1
        if p.state == 'R':
            R_list[t] += 1
        if p.state == 'D':
            D_list[t] += 1
        if p.state == 'V':
            V_list[t] += 1
        
        pop_list[t] += 1
        
        # Remove dead people
        if p.state == 'D':
            population.remove(p)
            pop_list[t] -= 1

plt.figure(tight_layout=True)
plt.plot(S_list, label='S')
plt.plot(I_list, label='I')
plt.plot(R_list, label='R')
plt.plot(D_list, label='D')
plt.plot(V_list, label='V')
plt.plot(pop_list, 'k--', label='Total')
plt.yscale('log')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Population')
plt.savefig('SIRD.png')