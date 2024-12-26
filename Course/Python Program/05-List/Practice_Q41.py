#Write a Python Program to Find the Second Largest Number in a List
# Input a list of numbers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Initialize the largest and second largest numbers
largest = second_largest = float('-inf')

# Traverse through the list to find the largest and second largest numbers
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

# Check if second largest number is found
if second_largest == float('-inf'):
    print("There is no second largest number.")
else:
    print("The second largest number in the list is:", second_largest)
