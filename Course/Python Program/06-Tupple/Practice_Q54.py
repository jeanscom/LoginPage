#Write a Python program to replace the last value of tuples in a list.
def replace_last_value(tuples_list, new_value):
    # Use a list comprehension to replace the last value in each tuple
    return [t[:-1] + (new_value,) for t in tuples_list]

# Example list of tuples
tuples_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# New value to replace the last value
new_value = 100

# Replace the last value in each tuple
updated_list = replace_last_value(tuples_list, new_value)

# Display the result
print("Original list:", tuples_list)
print("Updated list:", updated_list)
