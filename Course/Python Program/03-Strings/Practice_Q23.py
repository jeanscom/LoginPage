#Write a Python program to check whether a character is uppercase or lowercase alphabet.
# Input a character from the user
char = input("Enter a character: ")

# Check if the character is uppercase or lowercase
if char.isupper():
    print(f"{char} is an uppercase alphabet.")
elif char.islower():
    print(f"{char} is a lowercase alphabet.")
else:
    print(f"{char} is not an alphabet.")
