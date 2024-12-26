#Write a Python program to find all factors of a number.
# Input a number from the user
num = int(input("Enter a number: "))

# List to store the factors
factors = []

# Loop to find factors
for i in range(1, num + 1):
    if num % i == 0:  # If i divides num without a remainder
        factors.append(i)

# Print the factors
print(f"The factors of {num} are: {factors}")
