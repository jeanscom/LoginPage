#Write a Python program to find the first and last digits of a number.
# Input a number from the user
num = int(input("Enter a number: "))

# Find the last digit using modulus operator
last_digit = num % 10

# Find the first digit by repeatedly dividing the number by 10
first_digit = num
while first_digit >= 10:
    first_digit //= 10

# Print the first and last digits
print(f"The first digit is: {first_digit}")
print(f"The last digit is: {last_digit}")
