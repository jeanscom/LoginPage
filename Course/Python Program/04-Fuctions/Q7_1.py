# math_operations.py

# Function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Another example function in the same module
def add(a, b):
    return a + b
