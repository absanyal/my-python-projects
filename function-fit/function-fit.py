from math import sin
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
# Define the function to fit


def linear_function(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + c * np.sin(d * x)


def err_p(x, x_o):
    return abs((x - x_o) / x_o)


# Generate the data
x = np.random.uniform(-3, 3, 1000)
x_test = np.linspace(min(x), max(x), 1000)

params = [-1.623, 5.102, 3.2, 4.34]

y = np.zeros(len(x))

for i in range(len(x)):
    y[i] = linear_function(x[i], *params) + np.random.normal(0, 0.2)

# Fit the data to the function
popt, pcov = curve_fit(linear_function, x, y)

# Plot the data and the fitted function
plt.scatter(x, y, s=5, c='r')
plt.plot(x_test, linear_function(x_test, *popt),
         'b-', label='Fitted function', linewidth=2.0)
plt.show()

# Print the predicted coefficients
print("Predicted --- Actual --- Error %")
for i in range(len(params)):
    print("{:+.4f} --- {:+.4f} --- {:.4f} %".format(
        popt[i], params[i], err_p(popt[i], params[i]) * 100))
