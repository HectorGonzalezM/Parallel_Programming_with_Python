# Import the NumPy library for numerical operations and multiprocessing for parallel execution
import numpy as np
from multiprocessing import Pool

# Define a function f(x) that calculates the square root of (1 - x^2)
# This function corresponds to the top half of a circle's equation y = sqrt(1 - x^2)
def f(x):
    return np.sqrt(1 - x**2)

# Define a function to calculate the integral over a specific range using the rectangle method
def integrate(start, end, dx):
    # Generate an array of x values from start to end, spaced by dx
    x = np.arange(start, end, dx)
    # Evaluate the function f at each x value
    y = f(x)
    # Calculate the area under the curve by summing up the areas of the rectangles
    return np.sum(y * dx)

# Define a function to approximate pi using multiple processes
def parallel_pi(N, num_processes):
    dx = 1.0 / N  # Compute the step size based on the number of intervals
    chunk_size = N // num_processes  # Determine the number of intervals each process should handle

    # Create a list of tuples, each representing the (start, end, step size) for a range to integrate
    ranges = [(i * chunk_size * dx, (i + 1) * chunk_size * dx, dx) for i in range(num_processes)]
    
    # Use multiprocessing to execute the integration function across multiple processes
    with Pool(num_processes) as pool:
        results = pool.starmap(integrate, ranges)
    
    # Sum the results from all processes to get the total area under the curve
    total_area = sum(results)
    
    # Since the integral approximates the area of a quarter circle, multiply by 4 to estimate pi
    return 4 * total_area

# This block ensures the following code only executes when the script is run directly
if __name__ == "__main__":
    N = 100000000  # Set the number of intervals
    num_processes = 4  # Set the number of processes to use
    # Calculate the approximate value of pi using the parallel function
    pi_approximated = parallel_pi(N, num_processes)
    # Output the approximated value of pi
    print("Approximated Pi using multiprocessing:", pi_approximated)