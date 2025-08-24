import numpy as np

def main():
    """
    Create a 1D NumPy array and reshape it into a 2D array.
    """
    # Create a 1D array with elements from 1 to 12
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    
    # Reshape the array to 4 rows and 3 columns
    new_arr = arr.reshape(4, 3)
    
    # Print the reshaped array
    print(new_arr)

if __name__ == "__main__":
    main()
