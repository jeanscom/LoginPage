# Write a Python program to calculate the sum of three given numbers, if the values are
# equal then return three times their sum
# Input three numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Calculate the sum
sum_of_numbers = num1 + num2 + num3

# If all numbers are equal, return three times their sum
if num1 == num2 == num3:
    result = 3 * sum_of_numbers
else:
    result = sum_of_numbers

# Display the result
print(f"The result is: {result}")
    