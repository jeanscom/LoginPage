# Sample input list
input_list = [1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 3]

# Initialize lists for unique and duplicate elements
unique_elements = []
duplicate_elements = []

# Create a dictionary to count occurrences of each element
element_count = {}

#Write a program to read a list and split it into two in such a way that elements without duplicates are stored in one list and elements with duplicates are stored in the second list

# Count occurrences of each element in the input list
for element in input_list:
    if element in element_count:
        element_count[element] += 1
    else:
        element_count[element] = 1

# Split elements into unique and duplicate lists
for element, count in element_count.items():
    if count == 1:
        unique_elements.append(element)  # Add to unique list
    else:
        duplicate_elements.append(element)  # Add to duplicate list

# Output the results
print("Unique elements:", unique_elements)
print("Duplicate elements:", duplicate_elements)