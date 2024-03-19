import numpy as np
import matplotlib.pyplot as plt

# Define parameters
N = 500    # Number of sites
J = 1      # Coupling constant
B = 0      # External magnetic field
T_start = 3.0
T_stop = 0.1
T_num = 100
steps_therm = 10000
steps_record = 100
measurements = 10

# Initialize the lattice
lattice = np.random.choice([-1, 1], size=N)

# Define function for cooling the system
def cool_system(T_start, T_stop, T_num, steps_therm, steps_record, measurements):
    # Define temperature array
    T_array = np.linspace(T_start, T_stop, T_num)
    
    # Initialize arrays for storing energy and magnetization
    E_array = np.zeros(T_num)
    M_array = np.zeros(T_num)
    
    # Iterate over temperatures
    for i, T in enumerate(T_array):
        E_measurements = np.zeros(measurements)
        M_measurements = np.zeros(measurements)
        print("Current temperature is ", i+1, "/", len(T_array), ", T=", T, sep="")
        
        # Perform measurements at each temperature
        for k in range(measurements):
            # Thermalize the system
            for j in range(steps_therm):
                # Choose a random site to flip
                site = np.random.randint(N)
                # Calculate the energy difference
                delta_E = 2 * J * lattice[site] * (lattice[(site+1)%N] + lattice[(site-1)%N]) + 2 * B * lattice[site]
                # Decide whether to accept the move
                if delta_E < 0 or np.random.rand() < np.exp(-delta_E / T):
                    # Flip the spin
                    lattice[site] *= -1
            
            # Measure the energy and magnetization
            E_sum = 0
            M_sum = 0
            for j in range(steps_record):
                # Choose a random site to flip
                site = np.random.randint(N)
                # Calculate the energy difference
                delta_E = 2 * J * lattice[site] * (lattice[(site+1)%N] + lattice[(site-1)%N]) + 2 * B * lattice[site]
                # Decide whether to accept the move
                if delta_E < 0 or np.random.rand() < np.exp(-delta_E / T):
                    # Flip the spin
                    lattice[site] *= -1
                # Update the energy and magnetization
                E_sum += -J * np.sum(lattice * np.roll(lattice, -1)) - B * np.sum(lattice)
                M_sum += np.sum(lattice)
            E_measurements[k] = E_sum / (steps_record * N)
            M_measurements[k] = M_sum / (steps_record * N)
        
        # Average over the measurements
        E_array[i] = np.mean(E_measurements)
        M_array[i] = np.mean(M_measurements)
    
    # Plot energy and magnetization
    plt.plot(T_array, E_array, label='Energy')
    plt.plot(T_array, M_array, label='Magnetization')
    plt.xlabel('Temperature')
    plt.ylabel('Energy / Magnetization')
    plt.legend()
    plt.show()

# Call the function to cool the system
cool_system(T_start, T_stop, T_num, steps_therm, steps_record, measurements)
