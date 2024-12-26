# Write a Python program to input any character and check whether it is the alphabet, digit, or special character.
# Input a character from the user
char = input("Enter a character: ")

# Check if the character is alphabetical
if char.isalpha():
    print(f"{char} is an alphabetical character.")
else:
    print(f"{char} is not an alphabetical character.")
