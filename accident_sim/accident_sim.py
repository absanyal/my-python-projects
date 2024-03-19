import numpy as np
import matplotlib.pyplot as plt
from time import sleep

num_sims = 1000000
num_rides_per_sim = 50

total_rides = 0
total_deaths = 0
total_full_survival = 0

record_no_death_cases = 0

prob_death = 0.0001

rides_survived_list = []

sim_counter = 0
while (sim_counter < num_sims):

    if ((sim_counter % 100000) == 0):
        print("Starting simulation number ", sim_counter)
    
    # print("::::::::::::::Starting simulation number ", sim_counter,":::::::::::::::::::::")

    ride_counter = 1
    death_occured = 0
    while((ride_counter < (num_rides_per_sim)) and (death_occured == 0)):
        total_rides += 1
        # sleep(0.5)
        r = np.random.uniform(0, 1)
        if (r < prob_death):
            death_occured = 1
            total_deaths += 1
            rides_survived_list.append(ride_counter)
            # print("Sim ", sim_counter, ", ride ", ride_counter, ", DEATH")
        else:
            # print("Sim ", sim_counter, ", ride ", ride_counter, ", SURVIVED")
            death_occured = 0

        if (ride_counter == num_rides_per_sim - 1 and death_occured == 0 and record_no_death_cases == 1):
            # print("All rides SURVIVED")
            rides_survived_list.append(num_rides_per_sim)


        ride_counter += 1

    sim_counter += 1

# print(rides_survived_list)

print("Total rides:", total_rides)
print("Total deaths:", total_deaths)
print("Deaths/ride:", (total_deaths/total_rides))

rides_survived_list = np.array(rides_survived_list)

plt.hist(rides_survived_list, bins=2 * num_rides_per_sim, density=True)
plt.show()
