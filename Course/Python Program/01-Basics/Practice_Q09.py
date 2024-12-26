#Python Program to Swap Two Variables
# Input two variables
a = input("Enter the first variable (a): ")
b = input("Enter the second variable (b): ")

# Swap using a temporary variable
temp = a
a = b
b = temp

print(f"After swapping: a = {a}, b = {b}")
