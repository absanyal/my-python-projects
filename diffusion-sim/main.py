import numpy as np
import matplotlib.pyplot as plt

def compute_dispersion_from_hamiltonian(H, method='peak'):
    """
    Compute the dispersion relation from a Hamiltonian matrix.

    Parameters:
    -----------
    H : ndarray
        Hamiltonian matrix of shape (L, L) defined in the real-space (site) basis.
    method : str
        Method to extract momentum from the Fourier transform of the eigenvector.
        'peak' uses the momentum at which |FFT|^2 is maximized,
        'expectation' uses the weighted average (expectation value) of momentum.

    Returns:
    --------
    dispersion : ndarray
        Array of (k, E) pairs where k is the momentum and E is the eigenvalue.
    """
    L = H.shape[0]

    # Diagonalize the Hamiltonian.
    # Note: For Hermitian H, eigh returns sorted eigenvalues and eigenvectors.
    eigenvalues, eigenvectors = np.linalg.eigh(H)
    
    # eigenvectors columns correspond to eigenstates.
    # To iterate over eigenstates as rows, we take the transpose.
    eigenvectors = eigenvectors.T

    # Define allowed momenta assuming periodic boundary conditions.
    # np.fft.fftfreq returns frequencies; multiplying by 2*pi gives momenta.
    k_values = np.fft.fftfreq(L, d=1) * 2 * np.pi

    dispersion = []
    for psi, E in zip(eigenvectors, eigenvalues):
        # Transform the eigenvector from real space to momentum space.
        phi = np.fft.fft(psi) / np.sqrt(L)
        Pk = np.abs(phi)**2  # momentum probability distribution

        if method == 'peak':
            # Choose momentum corresponding to the maximum weight.
            k_index = np.argmax(Pk)
            k_val = k_values[k_index]
        elif method == 'expectation':
            # Alternatively, compute the expectation value of k.
            k_val = np.sum(k_values * Pk)
        else:
            raise ValueError("Unknown method. Choose 'peak' or 'expectation'.")

        dispersion.append((k_val, E))

    return np.array(dispersion)

def create_tight_binding_H(L, t=1.0):
    """
    Create a simple 1D tight-binding Hamiltonian with periodic boundary conditions.
    
    The Hamiltonian has the form:
        H = -t ∑ (|j⟩⟨j+1| + |j+1⟩⟨j|)
    
    Parameters:
    -----------
    L : int
        Number of lattice sites.
    t : float
        Hopping parameter.

    Returns:
    --------
    H : ndarray
        Hamiltonian matrix of shape (L, L).
    """
    H = np.zeros((L, L), dtype=complex)
    for i in range(L):
        H[i, (i+1) % L] = -t
        H[(i+1) % L, i] = -t
        H[0, -1] = -t
        H[-1, 0] = -t
    return H

# ---------------------- Example Usage ---------------------- #
if __name__ == "__main__":
    # Number of lattice sites and hopping parameter.
    L = 50
    t = 1.0

    # Create the Hamiltonian matrix.
    H = create_tight_binding_H(L, t)

    # Compute the dispersion relation from the Hamiltonian.
    dispersion = compute_dispersion_from_hamiltonian(H, method='peak')

    # Sort the dispersion data by momentum for a smooth plot.
    dispersion_sorted = dispersion[np.argsort(dispersion[:, 0])]

    # Plot the dispersion relation.
    plt.figure(figsize=(6, 6))
    plt.scatter(dispersion_sorted[:, 0], dispersion_sorted[:, 1], c='blue', label='Numerical Dispersion')
    plt.xlabel("Momentum k")
    plt.ylabel("Energy E")
    plt.title("Dispersion Relation from the Hamiltonian")
    plt.legend()
    plt.grid(True)
    plt.show()
