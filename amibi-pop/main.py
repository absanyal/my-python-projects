from xxlimited import foo
import numpy as np
import matplotlib.pyplot as plt
from modules.amibi import amibi

initial_gene = np.array([1, 1, 1])

amibilist = []

initial_pop = 100
initial_food = 100000

carrying_capacity = 1000

t_iters = 10000

for i in range(initial_pop):
    amibilist.append(amibi(initial_gene))

food = initial_food

food_list = [initial_food]
pop_list = [initial_pop]

eat_list = np.zeros(t_iters)
move_list = np.zeros(t_iters)
reproduce_list = np.zeros(t_iters)

for t in range(t_iters):
    
    new_amibilist = []
    
    if t % 1000 == 0:
        print("Simulation time: ", t)
        print("Population: ", len(amibilist))
        print("Food: ", food)
    
    for i, a in enumerate(amibilist):
        
        # print("Amibi {} is deciding at time: {}".format(i, t))
        
        decision = a.decide()
        
        if decision == 'eat':
            if (food > 0):
                a.eat()
                food -= 1
        elif decision == 'move':
            a.move()
        elif decision == 'reproduce':
            if (len(amibilist) <= carrying_capacity):
                new_a = a.reproduce()
                if new_a is not None:
                    new_amibilist.append(new_a)
            elif (len(amibilist) > carrying_capacity):
                r = np.random.uniform(0, 1)
                if r < 0.01:
                    new_a = a.reproduce()
                    if new_a is not None:
                        new_amibilist.append(new_a)
        
        gene = a.genes
        
        total_gene_weight = sum(gene)
        
        eat_list[t] += gene[0] / total_gene_weight
        move_list[t] += gene[1] / total_gene_weight
        reproduce_list[t] += gene[2] / total_gene_weight
                
        a.age_up()
        
        if a.energy <= 0:
            a.die()
            
        # Death by accident
        r = np.random.uniform(0, 1)
        if r < 0.01:
            a.die()
        
        
        if (a.age > 100):
            r = np.random.uniform(0, 1)
            if r < 0.50:
                a.die()
        
        if (len(amibilist) > carrying_capacity):
            r = np.random.uniform(0, 1)
            if r < 0.20:
                a.die()
            
        
        if not a.alive:
            amibilist.pop(i)
            food += 2
        
    amibilist.extend(new_amibilist)
    
    eat_list[t] /= len(amibilist)
    move_list[t] /= len(amibilist)
    reproduce_list[t] /= len(amibilist)
        
    if len(amibilist) < carrying_capacity:
        food += np.random.poisson(len(amibilist))
    else:
        food += np.random.poisson( int(0.1 * len(amibilist)) )
    
    food_list.append(food)
    pop_list.append(len(amibilist))
    
    if len(amibilist) == 0:
        print("All amibis died at time: ", t)
        break
    
    if (t % 50 == 0):
        with open('data/data.txt', 'w') as f:
            for i in range(t):
                f.write("{} {}\n".format(food_list[i], pop_list[i]))
        
        with open('data/gene.txt', 'w') as f:
            for i in range(t):
                f.write("{} {} {}\n".format(eat_list[i], move_list[i], reproduce_list[i]))
            
        