#Write a Python program to test whether a number is within 100 of 1000 or 2000.
# Input a number from the user
num = int(input("Enter a number: "))

# Check if the number is within 100 of 1000 or 2000
if abs(num - 1000) <= 100 or abs(num - 2000) <= 100:
    print(f"{num} is within 100 of 1000 or 2000.")
else:
    print(f"{num} is not within 100 of 1000 or 2000.")
