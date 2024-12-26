# Write a Python program to calculate the sum of digits of a number.
# Input a number from the user
num = int(input("Enter a number: "))

# Initialize sum variable to store the sum of digits
sum_digits = 0

# Loop to sum the digits of the number
while num > 0:
    sum_digits += num % 10  # Add the last digit to sum_digits
    num //= 10  # Remove the last digit from num

# Print the sum of digits
print(f"The sum of the digits is: {sum_digits}")
