#Write a Python program to find the repeated items of a tuple.
def find_repeated_items(input_tuple):
    # Create an empty dictionary to store the frequency of each item
    frequency = {}
    
    # Count the occurrences of each item in the tuple
    for item in input_tuple:
        frequency[item] = frequency.get(item, 0) + 1
    
    # Extract items that appear more than once
    repeated_items = {item for item, count in frequency.items() if count > 1}
    
    return repeated_items

# Example tuple
input_tuple = (1, 2, 3, 4, 2, 5, 6, 7, 3, 8, 9, 1)

# Find and print the repeated items
repeated_items = find_repeated_items(input_tuple)
print("Repeated items:", repeated_items)
