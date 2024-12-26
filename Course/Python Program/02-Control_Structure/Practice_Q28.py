# Write a Python program to count several digits in a number.
# Input a number from the user
num = int(input("Enter a number: "))

# Convert the number to a string to easily count the digits
num_str = str(num)

# Count the number of digits
digit_count = len(num_str)

# Print the result
print(f"The number {num} has {digit_count} digits.")
