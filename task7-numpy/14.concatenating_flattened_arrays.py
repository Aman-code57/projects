import numpy as np


def concatenate_flattened_arrays():
    """
    Flatten two 2D NumPy arrays and concatenate them into a single 1D array.
    """
    array1 = np.array([
        [1, 2],
        [3, 4]
    ])

    array2 = np.array([
        [5, 6],
        [7, 8]
    ])

    flat_array1 = array1.flatten()
    flat_array2 = array2.flatten()

    concatenated_array = np.concatenate((flat_array1, flat_array2))

    print(concatenated_array)


if __name__ == "__main__":
    concatenate_flattened_arrays()
