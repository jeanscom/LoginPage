problem 2
#Write python program to check whether vowel or consonant. [Hint, if c is a character,
c=c.lower() #will convert upper case to lower case . c=c.upper() Converts to upper case]
# Input a single character
char = input("Enter a single character: ").strip()

# Ensure the input is a single character
if len(char) == 1 and ((char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z')):
    # Convert the character to lowercase for uniformity
    char = char.lower()
    
    # Check if the character is a vowel
    if char in 'aeiou':
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Invalid input. Please enter a single alphabet character.")
