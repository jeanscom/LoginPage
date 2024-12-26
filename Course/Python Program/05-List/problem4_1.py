#Write a program to exchange the first half of the elements in the list with second half, assuming that the length of the list is an even number.

# Step 1: Define the list (ensure it has an even length)
my_list = [1, 2, 3, 4, 5, 6]  # Example list with an even number of elements

# Step 2: Calculate the midpoint
midpoint = len(my_list) // 2

# Step 3: Swap the halves
# Create a new list with the second half followed by the first half
swapped_list = my_list[midpoint:] + my_list[:midpoint]

# Step 4: Print the modified list
print("List after exchanging halves:", swapped_list)