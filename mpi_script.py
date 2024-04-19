# Import the MPI module for distributed computing and NumPy for numerical operations
from mpi4py import MPI
import numpy as np

# Define a function that represents the mathematical function sqrt(1 - x^2)
# Here, using float32 for computational efficiency with sufficient precision for this application
def f(x):
    return np.sqrt(1 - x**2, dtype=np.float32)

# Define a function to perform numerical integration over a specified interval
def integrate(start, end, dx):
    # Calculate the number of points in the interval
    num_points = int((end - start) / dx)
    # Create an array of x values within the specified range with the specified data type
    x = np.linspace(start, end, num_points, endpoint=False, dtype=np.float32)
    # Compute the function values at each x point
    y = f(x)
    # Sum the function values and multiply by the differential to get the area under the curve
    return np.sum(y) * dx

# Define the main function to compute an approximation of pi using MPI
def mpi_pi(N):
    # Initialize MPI communication
    comm = MPI.COMM_WORLD
    # Get the rank (ID) of the current process
    rank = comm.Get_rank()
    # Get the total number of processes involved
    size = comm.Get_size()

    # Calculate the differential for the integration
    dx = 1.0 / N
    # Calculate the number of intervals each process should handle
    local_n = N // size + (1 if rank < N % size else 0)
    # Calculate the starting x value for this process
    local_start = rank * (N // size) * dx + min(rank, N % size) * dx
    # Calculate the ending x value for this process
    local_end = local_start + local_n * dx

    # Each process performs its assigned integration task
    local_sum = integrate(local_start, local_end, dx)

    # Gather the integration results from all processes to the root process
    total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

    # The root process calculates the final approximation of pi
    if rank == 0:
        pi_approx = 4 * total_sum
        print("Approximated Pi using MPI:", pi_approx)

# Ensure the script runs only when executed directly (useful in multi-process scenarios)
if __name__ == '__main__':
    N = 10000000  # Set a large number of intervals for a more precise approximation
    mpi_pi(N)  # Call the main function to start the computation
