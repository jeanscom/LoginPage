#Write a Python program to calculate the factorial of a number.

num = int(input("Enter a number: "))

# Initialize the factorial variable
factorial = 1

# Use a while loop to calculate the factorial
i = 1
while i <= num:
    factorial *= i  # Multiply the factorial by the current number
    i += 1  # Increment the counter

# Print the factorial
print(f"The factorial of {num} is: {factorial}")
