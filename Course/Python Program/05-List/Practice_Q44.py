# Write a Python Program to Sort the List According to the Second Element in the Sublist
# Input a list of sublists
list_of_sublists = [
    [1, 3],
    [2, 2],
    [3, 1],
    [4, 4]
]

# Sort the list of sublists according to the second element in each sublist
list_of_sublists.sort(key=lambda x: x[1])

# Output the sorted list
print("Sorted list according to the second element:", list_of_sublists)
