
# Write a Python program to take an n-digit integer and print the digits of the
# number from left to right and right to left.

# Taking an n-digit integer as input
num = int(input("Enter an integer: "))

# Converting the number to a string to easily access digits
num_str = str(num)

# Printing the digits from left to right
print("Digits from left to right:")
for digit in num_str:
    print(digit, end=" ")

# Printing the digits from right to left
print("\nDigits from right to left:")
for digit in reversed(num_str):
    print(digit, end=" ")
