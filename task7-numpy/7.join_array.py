import numpy as np

def main():
    
    arr1 = np.array([1,2,3,4])
    arr2 = np.array([5,6,7,8])
    
    arr = np.stack((arr1,arr2),axis = 0)      #concatenate or stack
    
    print(arr)
    
if __name__ == "__main__":
    main()