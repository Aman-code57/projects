# Create the program to print list,tuple,set,dictionary using for loop
""" 
    create list, tuple, set, dictionary and 
    print seprately using for loop
    
"""

# Print header
print("list:--")

# Intialize list
mylist = [1,2,3,4,5]

# Create for loop for print number sequencely
for number in mylist:
    print(number)
    
# Print header 
print("tuples:--") 
  
# Intialize tuple
mytuple = ("aman","naveen","parmeet","vivek","vishal")

# Create the loop for print name sequencely
for name in mytuple:
    print(name)
    

# Print header 
print("set:--") 

# Intialize set
myset = {"chandigarh","mohali","panchkula","shimla"}

# Create the loop for print city sequencely
for city in myset:
    print(city)


# Print header 
print("dictionary:--") 

# Intialize dictionary
mydict = {
    "name" : "aman",
    "age" : 23,
    "state" : "punjab"
    }

# Create the loop for key,values sequencely
for keys,values in mydict.items():
    print(keys,values)


