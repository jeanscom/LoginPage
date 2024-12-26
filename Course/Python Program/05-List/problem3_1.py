# Given a list in Python and provided the positions of the elements, write a 
# program to swap the two elements in the list. Input : List = [23, 65, 19, 90], 
pos1 = 1, pos2 = 3  

# Step 1: Define the list
my_list = [23, 65, 19, 90]

# Step 2: Take input for the positions to swap
pos1 = int(input("Enter the first position to swap (0-based index): "))
pos2 = int(input("Enter the second position to swap (0-based index): "))

# Step 3: Swap the elements at the specified positions
# Check if the positions are valid
if 0 <= pos1 < len(my_list) and 0 <= pos2 < len(my_list):
    # Swapping the elements
    my_list[pos1], my_list[pos2] = my_list[pos2], my_list[pos1]
else:
    print("Invalid positions provided.")

# Step 4: Print the modified list
print("List after swapping:", my_list)