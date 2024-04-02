from matplotlib import tight_layout
import numpy as np
import matplotlib.pyplot as plt
from modules.chain import chain

chain_length = 20
E = 0
T = 310

T0 = 310

E_reduced = E / T0

num_sweeps = 50
num_trials = 10000

print("Chain length: {}".format(chain_length))
print("Energy cost: {} = {:.2f} kBT".format(E, E_reduced))
print("Temperature: {} K = {:.2f}".format(T, T / T0))
print("Simulation parameters: {} sweeps/trial, {} trials".format(num_sweeps, num_trials))


num_connected_list = []

c = chain(chain_length, E_reduced)


with open("data/chain_info.txt", "w") as f:
    f.write("# Chain length\t Temperature\n")
    f.write("{}\t{}\n".format(chain_length, T))
    

plt.figure(tight_layout=True)

T_reduced = T / T0

for i in range(num_trials):
    c.randomize()
    for j in range(num_sweeps):
        c.sweep(T_reduced)
    num_connected = c.get_connected()
    num_connected_list.append(num_connected)

    if (i+1) % 500 == 0:
        print("Trial", i+1, "completed.")
    
    if (i+1) % 50 == 0:
        with open("data/connected_data.txt", "w") as f:
            f.write("# Connected sites\n")
            for connected in num_connected_list:
                f.write(str(connected) + "\n")
    
    

print("Trials complete.")