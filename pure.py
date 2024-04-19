# Import the NumPy library for numerical operations
import numpy as np

# Define a function to approximate the value of pi using numerical integration
def approximate_pi(N):
    # Calculate the step size for the integration based on the number of intervals N
    dx = 1.0 / N
    
    # Generate an array of x values from 0 to 1 - dx, spaced evenly into N intervals
    x = np.linspace(0, 1 - dx, N)
    
    # Compute the values of the function f(x) = sqrt(1 - x^2) at each x value
    # This function represents the top half of a circle with radius 1
    f_x = np.sqrt(1 - x**2)
    
    # Compute the Riemann sum for the integral of f(x) from 0 to 1, using the area under f(x)
    # This sum estimates the area of a quarter circle with radius 1
    area_quarter_circle = np.sum(f_x * dx)
    
    # The area of the quarter circle is pi/4, so multiply by 4 to approximate pi
    pi_approx = 4 * area_quarter_circle
    
    # Return the approximate value of pi
    return pi_approx

# The following code only runs if this script is the main program and not imported as a module
if __name__ == "__main__":
    # Set the number of intervals for the approximation
    N = 10000000
    
    # Call the function to approximate pi
    pi_approximated = approximate_pi(N)
    
    # Print the approximated value of pi
    print("Approximated Pi:", pi_approximated)