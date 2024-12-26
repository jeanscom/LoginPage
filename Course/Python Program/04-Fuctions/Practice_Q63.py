#Write a Python program to find the greatest common divisor (gcd) of two integers using Recursion
def gcd(a, b):
    # Base case: if b becomes 0, return a
    if b == 0:
        return a
    # Recursive case: call the function with b and the remainder of a divided by b
    return gcd(b, a % b)

# Example usage
a = 56
b = 98
result = gcd(a, b)

print(f"The greatest common divisor of {a} and {b} is {result}.")
