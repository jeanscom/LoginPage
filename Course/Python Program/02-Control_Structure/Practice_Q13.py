#Python program to find whether the given number is Even or Odd
# Input a number from the user
num = int(input("Enter a number: "))

# Calculate the difference
difference = abs(num - 17)

# If the number is greater than 17, return double the absolute difference
if num > 17:
    result = 2 * difference
else:
    result = difference

# Display the result
print(f"The result is: {result}")
