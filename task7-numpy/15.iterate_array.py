import numpy as np


def iterate_3d_array():
    """
    Create a 3D NumPy array and iterate over each element using np.nditer.
    """
    array = np.array([[[1, 2], [3, 4], [5, 6], [7, 8]]])

    for element in np.nditer(array):
        print(element)


if __name__ == "__main__":
    iterate_3d_array()
