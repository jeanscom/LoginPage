#Recursive function to multiply two positive numbers
# Recursive function to multiply two numbers
def multiply_numbers(a, b):
    # Base case: if the second number (b) is 0, return 0
    if b == 0:
        return 0
    else:
        # Recursive case: add the first number (a) to the result of multiplying a and b-1
        return a + multiply_numbers(a, b - 1)

# Input two positive numbers
num1 = int(input("Enter the first positive number: "))
num2 = int(input("Enter the second positive number: "))

# Check if the numbers are positive
if num1 > 0 and num2 > 0:
    # Call the recursive function and print the result
    result = multiply_numbers(num1, num2)
    print(f"The product of {num1} and {num2} is: {result}")
else:
    print("Please enter positive numbers only.")
