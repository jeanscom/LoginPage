# Recursive function to the greatest common divisor of two positive numbers. 
# Recursive function to find the GCD using Euclid's algorithm
def gcd(a, b):
    if b == 0:
        return a  # Base case: when the second number becomes 0, return the first number as GCD
    else:
        return gcd(b, a % b)  # Recursive case

# Input: Get two numbers from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Call the GCD function and print the result
print(f"The GCD of {a} and {b} is: {gcd(a, b)}")