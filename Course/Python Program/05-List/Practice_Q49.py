# Python Program to print all odd indexed elements of a list
# Input a list of elements
elements = input("Enter elements separated by space: ").split()

# Print the odd-indexed elements of the list
print("Odd indexed elements:")
for i in range(1, len(elements), 2):  # Start from index 1 and step by 2
    print(elements[i])
