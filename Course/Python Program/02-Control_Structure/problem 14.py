
# Write a Python program to compute the GCD (also called HCF) of two
# given numbers.

# Input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Ensure numbers are positive
if a < 0 or b < 0:
    print("Please enter non-negative integers.")
else:
    # Using the Euclidean algorithm
    while b != 0:
        a, b = b, a % b

    print(f"The GCD (HCF) of the given numbers is: {a}")
