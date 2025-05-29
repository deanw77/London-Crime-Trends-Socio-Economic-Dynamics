
import numpy as np

def make_x_and_y(n):
    """
    Generates two numpy arrays of size n.
    
    The first array contains random integers between 0 and 100.
    The second array contains random integers between 0 and 1000.
    
    Parameters:
    n (int): The size of the arrays to be generated.
    
    Returns:
    tuple: A tuple containing two numpy arrays (x, y).
    """
    x = np.random.randint(n)
    y = np.random.randint(n)
    return x, y