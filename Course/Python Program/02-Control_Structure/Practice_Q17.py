# Python Program to Find the Factorial of a Number
# Input a number from the user
num = int(input("Enter a number: "))

# Initialize factorial variable
factorial = 1

# Check if the number is negative
if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    # Calculate factorial using a for loop
    for i in range(1, num + 1):
        factorial *= i

    # Display the result
    print(f"The factorial of {num} is: {factorial}")
