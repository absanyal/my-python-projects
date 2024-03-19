import numpy as np
import matplotlib.pyplot as plt


def filter_angle(theta):
    """
    Filters the angle to be within the range of 0 to 90 degrees.

    Parameters:
    theta (float): The input angle in degrees.

    Returns:
    float: The filtered angle within the range of 0 to 90 degrees.

    The function works as follows:
    1. If the input angle theta is already between 0 and 90 degrees inclusive, the function simply returns theta.
    2. If theta is less than 0 degrees, the function adds 90 to theta and recursively calls itself with the result. This effectively rotates the negative angle into the range of 0 to 90 degrees. The function will continue to add 90 to theta and call itself until theta is no longer less than 0.
    3. If theta is greater than 90 degrees, the function subtracts 90 from theta and recursively calls itself with the result. This effectively rotates the angle into the range of 0 to 90 degrees. The function will continue to subtract 90 from theta and call itself until theta is no longer greater than 90.

    This function uses recursion to handle angles outside the range of 0 to 90 degrees, repeatedly adjusting the angle by 90 degrees until it falls within the desired range.
    """
    if 0 <= theta <= 90:
        return theta
    elif theta < 0:
        return filter_angle(theta + 90)
    elif theta > 90:
        return filter_angle(theta - 90)


theta = np.linspace(-180, 180, 1000)
theta_filtered = np.array([filter_angle(t) for t in theta])

x_ticklist = np.arange(min(theta), max(theta) + 1, 45)
y_ticklist = np.arange(0, 90+1, 45)

plt.figure(tight_layout=True)
plt.plot(theta, theta_filtered)
plt.xlabel('Original angle (degrees)')
plt.ylabel('Filtered angle (degrees)')
plt.xticks(x_ticklist, labels=[
           r'{:.0f}$\degree$'.format(_) for _ in x_ticklist])
plt.yticks(y_ticklist,
           labels=[r'{:.0f}$\degree$'.format(_) for _ in y_ticklist])
plt.grid(axis='both')
plt.show()
