#Program to define a module and import a specific function in that module to another program
# main_program.py

# Importing the factorial function from math_operations module
from Q7_1 import factorial

# Get user input
n = int(input("Enter a number to calculate its factorial: "))

# Call the imported factorial function
result = factorial(n)

# Print the result
print(f"The factorial of {n} is: {result}")
