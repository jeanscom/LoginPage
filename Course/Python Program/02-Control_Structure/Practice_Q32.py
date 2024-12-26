#Write a Python program to check whether a number is palindrome or no
# Input a number from the user
num = int(input("Enter a number: "))

# Store the original number
original_num = num

# Initialize the variable to store the reversed number
reversed_num = 0

# Loop to reverse the number
while num > 0:
    digit = num % 10  # Get the last digit
    reversed_num = reversed_num * 10 + digit  # Build the reversed number
    num //= 10  # Remove the last digit

# Check if the original number is equal to the reversed number
if original_num == reversed_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")
