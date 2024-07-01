import numpy as np
import matplotlib.pyplot as plt

from modules.walker import walker, breed

num_walkers = 500
num_generations = 1000

mutation_rate = 0.05
max_steps_allowed = 100

# Create the initial population
population = []
for i in range(num_walkers):
    path = np.random.uniform(0, 1, max_steps_allowed)
    population.append(walker(0, 0, path))

target_x1 = 90
target_y1 = 0

# target_x2 = 20
# target_y2 = 20

target_threshold = 1

gene_positions = np.arange(0, max_steps_allowed)


# plt.figure(tight_layout=True)
fig1 = plt.figure(tight_layout=True)
ax1 = fig1.add_subplot(111)

fig2 = plt.figure(tight_layout=True)
ax2 = fig2.add_subplot(111)


for generation in range(num_generations):
    ax1.clear()
    ax2.clear()
    target1_visited = False
    target2_visited = False
    

    ax1.scatter(0, 0, color='green', s=100, marker='o')
    ax1.scatter(target_x1, target_y1, color='red', s=100, marker='x')
    c1 = plt.Circle((target_x1, target_y1), target_threshold,
                    color='red', alpha=0.5, fill=False)
    fig1.gca().add_artist(c1)
    
    # plt.scatter(target_x2, target_y2, color='red', s=100, marker='x')
    # c2 = plt.Circle((target_x2, target_y2), target_threshold,
    #                 color='red', alpha=0.5, fill=False)
    # plt.gca().add_artist(c2)

    print("Generation: ", generation)
    fitness_list = np.zeros(num_walkers)
    for w_i in range(num_walkers):
        # population[w_i].reset()

        for i in range(max_steps_allowed):
            population[w_i].walk()
            
            distance_from_target1 = np.sqrt(
                (population[w_i].x - target_x1)**2 + (population[w_i].y - target_y1)**2)
            # distance_from_target2 = np.sqrt(
            #     (population[w_i].x - target_x2)**2 + (population[w_i].y - target_y2)**2)
            if distance_from_target1 < target_threshold:
                target1_visited = True
                break
            
            
        x = population[w_i].x
        y = population[w_i].y

        fitness = (((distance_from_target1 + 1e-6)**(-5.0))) * (population[w_i].steps_walked + 1e-6) ** (-1.0)
        
        fitness_list[w_i] = fitness
        

        ax1.plot(population[w_i].xpath,
                 population[w_i].ypath, color='b', alpha=0.01)

        # plt.xlim(-50, 50)
        # plt.ylim(-50, 50)
        
        # ax2.scatter(gene_positions, population[w_i].path, color='b', alpha=0.1, s=5, marker='o')
        ax2.plot(gene_positions, population[w_i].path, color='b', alpha=0.01,
                 linewidth=0.5, linestyle='-', marker='o', markersize=1)
        ax2.set_xlim(0, max_steps_allowed)
        ax2.set_ylim(0, 1)

        if w_i == num_walkers - 1:

            fig1.savefig("plots/paths.pdf")
            fig1.savefig("plots/paths.png")
            
            fig2.savefig("plots/genes.pdf")
            fig2.savefig("plots/genes.png")

    # Selection

    fitness_list = fitness_list / np.sum(fitness_list)

    new_population = []

    for i in range(num_walkers):
        w1 = np.random.choice(population, p=fitness_list)
        w2 = np.random.choice(population, p=fitness_list)

        new_population.append(breed(w1, w2, mutation_rate, 0, 0))

    population = new_population.copy()
