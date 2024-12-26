#Program to find the factorial of a number using Recursion
# Function to find the factorial using recursion
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input a number from the user
num = int(input("Enter a number: "))

# Calculate and print the factorial
result = factorial(num)
print(f"The factorial of {num} is: {result}")
