#Recursive function to add two positive numbers.
# Recursive function to add two numbers
def add_numbers(a, b):
    # Base case: if second number (b) is 0, return the first number
    if b == 0:
        return a
    else:
        # Recursive case: add 1 to the first number and subtract 1 from the second
        return add_numbers(a + 1, b - 1)

# Input two positive numbers
num1 = int(input("Enter the first positive number: "))
num2 = int(input("Enter the second positive number: "))

# Check if the numbers are positive
if num1 > 0 and num2 > 0:
    # Call the recursive function and print the result
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")
else:
    print("Please enter positive numbers only.")
