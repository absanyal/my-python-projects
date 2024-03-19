import matplotlib.pyplot as plt
import numpy as np

# Load the data from the file
data = np.loadtxt('linker-attachment-time.txt')

bins_list = np.arange(int(min(data)), int(max(data))+1, 2)

# Plot the histogram
plt.figure(tight_layout=True)
plt.hist(data, bins=bins_list, rwidth=0.85, color='blue', align='mid', density=True)
plt.xlabel('Attachment Time', fontsize=18)
plt.ylabel('Frequency', fontsize=18)
plt.savefig('linker-attachment-time-plot.pdf')