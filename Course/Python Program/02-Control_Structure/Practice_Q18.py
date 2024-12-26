#Python Program to print a maximum of 3 numbers
# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the maximum of the three numbers
max_num = max(num1, num2, num3)

# Display the result
print(f"The maximum of {num1}, {num2}, and {num3} is: {max_num}")
