#Write a Python Program to Find the Largest Number in a List
# Input a list of numbers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Find the largest number using the max() function
largest_number = max(numbers)

# Print the largest number
print("The largest number in the list is:", largest_number)
