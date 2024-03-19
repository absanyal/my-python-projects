import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc, tight_layout
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import MultipleLocator
minorLocator1  = AutoMinorLocator()
minorLocator2   = AutoMinorLocator()


# Set the font
rc('font', family='serif')
rc('figure', figsize=(10, 6))
rc('font', size=18)
rc('xtick.major', size=5)
rc('xtick.minor', size=3)

theta = np.loadtxt('data/theta_list.txt')

color_list = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'lime', 'teal', 'lavender', 'tan', 'salmon', 'gold', 'lightblue', 'lightgreen', 'lightcoral', 'lightpink', 'lightgray', 'lightyellow', 'lightcyan', 'lightseagreen', 'lightsteelblue', 'lightgoldenrodyellow', 'lightblue', 'lightgreen', 'lightcoral', 'lightpink', 'lightgray', 'lightyellow', 'lightcyan', 'lightseagreen', 'lightsteelblue', 'lightgoldenrodyellow', 'lightblue', 'lightgreen', 'lightcoral', 'lightpink', 'lightgray', 'lightyellow', 'lightcyan', 'lightseagreen', 'lightsteelblue', 'lightgoldenrodyellow', 'lightblue', 'lightgreen', 'lightcoral', 'lightpink', 'lightgray', 'lightyellow', 'lightcyan', 'lightseagreen', 'lightsteelblue', 'lightgoldenrodyellow', 'lightblue', 'lightgreen', 'lightcoral', 'lightpink', 'lightgray', 'lightyellow', 'lightcyan', 'lightseagreen', 'lightsteelblue', 'lightgoldenrodyellow', 'lightblue', 'lightgreen', 'lightcoral', 'lightpink', 'lightgray', 'lightyellow', 'lightcyan', 'lightseagreen', 'lightsteelblue', 'lightgoldenrodyellow', 'lightblue', 'lightgreen', 'lightcoral', 'lightpink', 'lightgray', 'lightyellow', 'lightcyan', 'lightseagreen', 'lightsteelblue', 'lightgoldenrodyellow', 'lightblue', 'lightgreen', 'lightcoral', 'lightpink', 'lightgray', 'lightyellow', 'lightcyan', 'lightseagreen', 'lightsteelblue', 'lightgoldenrodyellow', 'lightblue', 'lightgreen', 'lightcoral', 'lightpink', 'lightgray', 'lightyellow', 'lightcyan', 'lightseagreen', 'lightsteelblue', 'lightgoldenrodyellow', 'lightblue', 'lightgreen', 'lightcoral', 'lightpink', 'lightgray', 'lightyellow', 'lightcyan', 'lightseagreen', 'lightsteelblue', 'lightgoldenrodyellow', 'lightblue', 'lightgreen']

# color_list_full  = np.array(list(matplotlib.colors.CSS4_COLORS.keys()))

# color_list = color_list_full[np.random.choice(len(color_list_full), len(theta), replace=False)]

plt.figure(tight_layout=True)
fig, ax = plt.subplots(tight_layout=True)
ax.xaxis.set_minor_locator(minorLocator1)
ax.yaxis.set_minor_locator(minorLocator2)

for theta_i in range(len(theta)):
    t, f = np.loadtxt('data/firstpassage_{}.txt'.format(theta_i), unpack=True)
    ax.plot(t, f, label=r'FP ${:3.0f}\degree$'.format(theta[theta_i]), color=color_list[theta_i])
    t, w = np.loadtxt('data/wald_{}.txt'.format(theta_i), unpack=True)
    ax.plot(t, w, label=r'W  ${:3.0f}\degree$'.format(theta[theta_i]), linestyle='dotted', color=color_list[theta_i], linewidth=2)

plt.xlabel(r'$t$')
plt.ylabel("Distribution")
plt.legend(title=r'$\theta_0$', loc='best', borderpad=0.5)

plt.xscale('log')

plt.savefig('plots/firstpassage.pdf')