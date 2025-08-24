import numpy as np


def flatten_and_display_array():
    """
    Create a 2D NumPy array, flatten it using flatten(), and print both.
    """
    array = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    flattened_array = array.flatten()

    print("Original array:")
    print(array)

    print("\nFlattened array:")
    print(flattened_array)


if __name__ == "__main__":
    flatten_and_display_array()
