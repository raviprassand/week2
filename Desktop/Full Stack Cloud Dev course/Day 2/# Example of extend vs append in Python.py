# Example of extend vs append in Python

# Creating a list
original_list = [1, 2, 3]

# Using append to add an element
original_list.append(4)
print("After append:", original_list)  # Output: [1, 2, 3, 4]

# Using append to add a list
original_list.append([5, 6])
print("After append a list:", original_list)  # Output: [1, 2, 3, 4, [5, 6]]

# Resetting the list
original_list = [1, 2, 3]

# Using extend to add elements from another list
original_list.extend([4, 5, 6])
print("After extend:", original_list)  # Output: [1, 2, 3, 4, 5, 6]