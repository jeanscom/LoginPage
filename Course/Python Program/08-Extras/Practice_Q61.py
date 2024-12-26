#Write a Python program to calculate the harmonic sum of n-1
def harmonic_sum(n):
    # Calculate the harmonic sum of (n-1)
    if n <= 1:
        print("n must be greater than 1.")
        return None

    total = 0
    for i in range(1, n):
        total += 1 / i  # Add the reciprocal of each number
    
    return total

# Example usage
n = 5
result = harmonic_sum(n)

if result is not None:
    print(f"The harmonic sum of {n-1} is {result:.4f}.")
