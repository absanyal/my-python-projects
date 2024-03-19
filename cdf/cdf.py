import numpy as np


def cdf(data, bin_list='auto'):
        """
        Calculate the cumulative distribution function (CDF) of a given dataset.

        Parameters:
        - data (array-like): The input dataset.
        - bin_list (int or sequence or str, optional): The number of bins or the bin edges for histogram calculation. 
            If 'auto', the number of bins is determined automatically. Default is 'auto'.

        Returns:
        - X1 (ndarray): The bin edges of the histogram.
        - F1 (ndarray): The cumulative distribution function values.
        """
        H, X1 = np.histogram(data, bins=bin_list, density=True)
        dx = X1[1] - X1[0]
        F1 = np.cumsum(H)*dx

        return X1[1:], F1
