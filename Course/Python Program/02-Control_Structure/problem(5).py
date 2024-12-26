
# Write a Python program to print those numbers which are divisible by 7,
# and by 5, between a and b, where a and b are two numbers given by the
# user.

# Taking input from the user for the range
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Printing numbers divisible by both 7 and 5
print(f"Numbers divisible by 7 and 5 between {a} and {b}:")

# Loop through the range from a to b (inclusive)
for num in range(a, b + 1):
    if num % 7 == 0 and num % 5 == 0:
        print(num)
