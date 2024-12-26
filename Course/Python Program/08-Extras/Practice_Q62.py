#Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0)
def sum_series(n):
    total = 0
    while n > 0:
        total += n  # Add the current term to the total
        n -= 2  # Subtract 2 to get the next term
    return total

# Example usage
n = 10
result = sum_series(n)

print(f"The sum of the series for n = {n} is {result}.")
