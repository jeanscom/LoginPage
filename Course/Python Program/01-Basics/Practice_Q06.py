#Python Program to Find the Square Root
import math

# Input from the user
num = float(input("Enter a number to find its square root: "))

# Check if the number is non-negative
if num >= 0:
    # Calculate the square root
    sqrt_value = math.sqrt(num)
    print(f"The square root of {num} is: {sqrt_value}")
else:
    print("The square root of a negative number is not real.")
