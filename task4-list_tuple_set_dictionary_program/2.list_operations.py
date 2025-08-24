# add item in list
"""
Demonstrates basic list operations in Python:
- Initializing a list with names
- Adding an item to the end of the list using append()
- Inserting an item at a specific index using insert()
- Removing a specific item by value using remove()

Operations performed:
1. Initialize a list `mylist` with four names.
2. Append "vishal" to the end of `mylist`.
3. Insert "akash" at index 2 in `mylist`.
4. Remove the item "aman" from `mylist`.
5. Print the list after each operation to show the changes.
"""


# Intialize list
mylist = ["aman","naveen","parmeet","vivek"]

# Add another name using append
mylist.append("vishal")

# Print list after add new
print(mylist)


#insert item in list

# insert a name in specific index
mylist.insert(2,"akash")

# Print the list after insertion
print(mylist)



# Remove the Specific Item in list
mylist.remove("aman")

# print list after the removing specific item
print(mylist)