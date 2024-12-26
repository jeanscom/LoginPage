#Write a Python program to check whether a character is alphabetical or not.
# Input a number from the user
num = int(input("Enter a number: "))

# Check if the number is divisible by both 5 and 11
if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisible by both 5 and 11.")
else:
    print(f"{num} is not divisible by both 5 and 11.")
