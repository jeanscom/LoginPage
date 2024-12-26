#Write a Python program to get the 4th element and 4th element from the last of a tuple
def get_elements(tup):
    # Check if the tuple has at least 4 elements
    if len(tup) < 4:
        return "Tuple must have at least 4 elements."
    
    # Get the 4th element (index 3)
    fourth_element = tup[3]
    
    # Get the 4th element from the last (index -4)
    fourth_from_last = tup[-4]
    
    return fourth_element, fourth_from_last

# Example tuple
example_tuple = (10, 20, 30, 40, 50, 60, 70, 80)

# Get the elements
fourth, fourth_last = get_elements(example_tuple)

# Print the results
print("4th element:", fourth)
print("4th element from the last:", fourth_last)