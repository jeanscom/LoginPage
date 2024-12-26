# Write a Python Program to Sort a List According to the Length of the Elements
# Input a list of elements
elements = input("Enter elements separated by space: ").split()

# Sort the list based on the length of each element
elements.sort(key=len)

# Output the sorted list
print("Sorted list based on the length of elements:", elements)
