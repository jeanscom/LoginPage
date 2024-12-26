# Write a program that rotates the elements of a list so that the element at the first 
# index moves to the second index, the element in the second index moves to the 
# third index, etc., and the element in the last index moves to the first index.

# Sample input list
input_list = [1, 2, 3, 4, 5]

# Check if the list is not empty
if input_list:
    # Rotate the list
    rotated_list = [input_list[-1]] + input_list[:-1]
else:
    rotated_list = []

# Output the result
print("Original list:", input_list)
print("Rotated list:", rotated_list)