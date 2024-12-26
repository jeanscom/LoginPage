# Write a Python program to remove an empty tuple(s) from a list of tuples.
# Sample data: [(), (), (",), ('a','b'), ('a','b, 'c'),('d')]
def tuples_to_dict(tuples_list):
    # Use the dict() constructor to convert the list of tuples into a dictionary
    return dict(tuples_list)

# Example list of tuples
tuples_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

# Convert to dictionary
converted_dict = tuples_to_dict(tuples_list)

# Display the result
print("List of tuples:", tuples_list)
print("Converted dictionary:", converted_dict)
