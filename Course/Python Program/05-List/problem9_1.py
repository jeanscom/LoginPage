# Given two unsorted lists of distinct elements, the task is to find all pairs from both 
# lists whose sum is equal to x. 
#Input : 
list1 = [-1, -2, 4, -6, 5, 7]
list2 = [6, 3, 4, 0]
x = 8
 #Output : [(5, 3), (4, 4)

# Input lists and target sum
list1 = [-1, -2, 4, -6, 5, 7]
list2 = [6, 3, 4, 0]
x = 8

# Create a set from the second list for fast look-up
set_list2 = set(list2)

# Initialize a list to store the pairs
pairs = []

# Iterate through the first list
for num1 in list1:
    # Calculate the complement
    complement = x - num1
    # Check if the complement exists in the second list
    if complement in set_list2:
        pairs.append((num1, complement))

# Output the result
print("Pairs whose sum is equal to", x, ":", pairs)