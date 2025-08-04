# Build a pattern generator that prints a triangle of * based on user input

# Input rows from user
rows = int(input("enter the rows: "))

# Loop for rows space/tabs
for i in range(1,rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end = "")
        
 #Loop for printing star       
    for k in range(1, 2 * i):  
        print("*", end="")
    
        
#print into next line       
    print()