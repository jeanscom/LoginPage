#Write a Python program to check whether an element exists within a tuple
def element_exists(input_tuple, element):
    # Check if the element is in the tuple
    return element in input_tuple

# Example tuple
input_tuple = (10, 20, 30, 40, 50)

# Element to check
element_to_check = 30

# Check and display result
if element_exists(input_tuple, element_to_check):
    print(f"The element {element_to_check} exists in the tuple.")
else:
    print(f"The element {element_to_check} does not exist in the tuple.")
