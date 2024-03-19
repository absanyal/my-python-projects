"""
This module contains two functions: lorentzian and dos.

The lorentzian function calculates the value of the Lorentzian function at a given point. 
The Lorentzian function, also known as the Cauchy distribution, is a function that is used 
in physics and mathematics, often to model resonances or line shapes. It takes three parameters: 
x, x0, and gamma. x is the point at which the function is evaluated, x0 is the center of the 
Lorentzian function, and gamma is the width parameter of the Lorentzian function. The function 
returns the value of the Lorentzian function at the given point x.

The dos function calculates the density of states. In quantum mechanics, the density of states 
of a system describes the number of states that are to be occupied by the system at each energy level. 
It takes three parameters: x_list, w_list, and gamma. x_list is a list of x values, w_list is a list 
of w values, and gamma is the width parameter. The function initializes a zero-filled numpy array 
density of the same length as w_list. Then, for each x in x_list, it adds the value of the Lorentzian 
function evaluated at w_list, x, and gamma to density. Finally, it returns density divided by the length 
of x_list, effectively calculating the average density of states.
"""
import numpy as np

def lorentzian(x: float, x0: float, gamma: float) -> float:
    """
    Calculate the Lorentzian function at a given point.

    Parameters:
    x (float): The point at which to evaluate the Lorentzian function.
    x0 (float): The center of the Lorentzian function.
    gamma (float): The width parameter of the Lorentzian function.

    Returns:
    float: The value of the Lorentzian function at the given point.
    """
    return 1 / np.pi * 0.5 * gamma / ((x - x0) ** 2 + (0.5 * gamma) ** 2)

def dos(x_list: list[float], w_list: list[float], gamma: float) -> np.ndarray:
    """
    Calculate the density of states.

    Parameters:
    x_list (List[float]): List of x values.
    w_list (List[float]): List of w values.
    gamma (float): The width parameter.

    Returns:
    np.ndarray: The density of states.
    """
    density = np.zeros(len(w_list))
    for x in x_list:
        density += lorentzian(w_list, x, gamma)
    return density / len(x_list)
