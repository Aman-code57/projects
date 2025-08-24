import numpy as np


def slice_array_elements():
    """
    Create a 2D NumPy array and print a slice of elements from the first row (index 0),
    selecting columns from index 1 to 2 (inclusive of 1, exclusive of 3).
    """
    array = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ])

    sliced_elements = array[0, 1:3]

    print("Sliced elements from first row (columns 1 to 2):")
    print(sliced_elements)


if __name__ == "__main__":
    slice_array_elements()
