"""
This script demonstrates how to add and remove items in a Python set.
It initializes a set with some color names, adds a new color, and then removes 
two colors using `remove()` and `discard()` methods respectively.
"""

# Initialize a set with some color names
myset = {"blue", "black", "red", "yellow"}

# Add a new item to the set
myset.add("purple")

# Print the set after adding a new item
print("Set after adding 'purple':", myset)

# Remove items from the set
# `remove()` will raise an error if the item does not exist
myset.remove("black")

# `discard()` will NOT raise an error if the item does not exist
myset.discard("blue")

# Print the set after removing two items
print("Set after removing 'black' and 'blue':", myset)
