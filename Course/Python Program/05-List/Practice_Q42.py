#  Write a Python Program to Put Even and Odd elements in a List into Two Different Lists
# Input a list of numbers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Initialize two lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Traverse through the input list
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)  # Add to even list if the number is even
    else:
        odd_numbers.append(num)   # Add to odd list if the number is odd

# Output the even and odd lists
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
