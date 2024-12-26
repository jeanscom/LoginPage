#Write a Python program to enter a number and print its reverse.
# Input a number from the user
num = int(input("Enter a number: "))

# Initialize the variable to store the reversed number
reversed_num = 0

# Loop to reverse the number
while num > 0:
    digit = num % 10  # Get the last digit
    reversed_num = reversed_num * 10 + digit  # Build the reversed number
    num //= 10  # Remove the last digit

# Print the reversed number
print(f"The reverse of the number is: {reversed_num}")
