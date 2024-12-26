# Write a Python Program to Find the Union of two Lists
# Input two lists
list1 = list(map(int, input("Enter the first list of numbers separated by space: ").split()))
list2 = list(map(int, input("Enter the second list of numbers separated by space: ").split()))

# Find the union of two lists using the union operator
union_list = list(set(list1) | set(list2))

# Output the union of the lists
print("Union of the two lists:", union_list)
