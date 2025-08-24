import numpy as np


def ravel_array():
    """
    Create a 2D NumPy array and flatten it into a 1D array using ravel().
    """
    array = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    flattened_array = array.ravel()

    print(flattened_array)


if __name__ == "__main__":
    ravel_array()
