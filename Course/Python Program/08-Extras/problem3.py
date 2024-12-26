# The Fibonacci series numbers are given as: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, . . . In a Fibonacci series, every term is the sum of the preceding two terms, starting from 0 and 1 as the first and second terms. Write a python program to print Fibonacci series in a given range [ start, end] including start and end values.


# Input from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Initialize the first two Fibonacci numbers
a, b = 0, 1

# Create a list to store Fibonacci numbers in the specified range
fib_series = []

# Generate Fibonacci numbers until the last number exceeds 'end'
while a <= end:
    if a >= start:
        fib_series.append(a)  # Add the number to the list if it's within the range
    a, b = b, a + b  # Update to the next Fibonacci numbers

# Print the result
print(f"Fibonacci numbers in the range [{start}, {end}]: {fib_series}")