# Operation in tuples
"""
Perform operations on a tuple by converting it to a list.

Steps:
1. Initialize a tuple with some state names.
2. Convert the tuple to a list to allow modifications.
3. Add a new state ("himachal") to the list.
4. Remove an existing state ("haryana") from the list.
5. Convert the modified list back to a tuple.
6. Print the final tuple after modifications.

Note: Tuples are immutable, so conversion to a list is necessary for modification.
"""


# Intialize the tuple
mytuple = ("uttarkhand","haryana","punjab")

# Convert tuple to list for add new item using list constructor
mylist = list(mytuple)
mylist.append("himachal")

mylist.remove("haryana")

# covert list into tuple
mytuple = tuple(mylist)

# Print the tuple after addition and remove
print(mytuple)