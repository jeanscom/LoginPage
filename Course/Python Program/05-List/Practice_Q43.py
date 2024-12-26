#Write a Python Program to Merge Two Lists and Sort it
# Input a list of numbers
# Input two lists from the user
list1 = list(map(int, input("Enter the first list of numbers separated by space: ").split()))
list2 = list(map(int, input("Enter the second list of numbers separated by space: ").split()))

# Merge the two lists
merged_list = list1 + list2

# Sort the merged list
merged_list.sort()

# Output the sorted merged list
print("Merged and sorted list:", merged_list)
