import numpy as np


def flatten_array_fortran_order():
    """
    Flatten a 2D NumPy array using Fortran-style (column-major) order.
    """
    array = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    flattened_array = array.flatten(order='F')

    print(flattened_array)


if __name__ == "__main__":
    flatten_array_fortran_order()
