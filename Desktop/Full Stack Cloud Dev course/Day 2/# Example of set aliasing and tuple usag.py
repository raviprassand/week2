# Example of set aliasing and tuple usage in Python

# Creating a set
original_set = {1, 2, 3, 4, 5}

# Aliasing the set
alias_set = original_set

# Modifying the alias set
alias_set.add(6)

# Both sets will reflect the change
print("Original Set:", original_set)
print("Alias Set:", alias_set)

# Creating a tuple
example_tuple = (10, 20, 30, 40, 50)

# Accessing elements in a tuple
first_element = example_tuple[0]
last_element = example_tuple[-1]

print("First Element of Tuple:", first_element)
print("Last Element of Tuple:", last_element)