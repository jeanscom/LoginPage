
# Write a Python program to find the sum of the below series provided n is a
# number given by the user.
# 1+1/2!+1/3!

# Input from the user
n = int(input("Enter a positive integer (n): "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    # Compute the sum of the series
    series_sum = 1  # The first term is always 1
    factorial = 1   # To store the factorial incrementally

    for i in range(2, n + 1):
        factorial *= i  # Compute i!
        series_sum += 1 / factorial  # Add 1/i! to the sum

    print(f"The sum of the series 1 + 1/2! + 1/3! + ... + 1/{n}! is: {series_sum}")
