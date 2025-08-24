import numpy as np

def main():
    
    arr = np.array([1,2,3,4,5])
    
    newarr = arr.copy()
    arr[0] = 23
    
    print("after copy method")
    print(arr)
    print(newarr)
    
    
    arr2 =np.array([1,2,3,4,5])
    
    newarr2 = arr2.view()
    arr2[0] = 23
    
    print("after the view")
    print(arr2)
    print(newarr2)
    
if __name__ == "__main__":
    main()