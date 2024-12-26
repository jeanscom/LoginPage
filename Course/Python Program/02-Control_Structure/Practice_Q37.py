# Write a Python program to print all Prime numbers between 1 to n.
# Input the upper limit n
# Input the upper limit n
n = int(input("Enter a number: "))

# Start with the first number to check (2 is the smallest prime)
num = 2

# Loop through all numbers from 2 to n
while num <= n:
    is_prime = True
    i = 2
    # Check if num is divisible by any number from 2 to sqrt(num)
    while i * i <= num:
        if num % i == 0:  # If num is divisible by i, it's not a prime
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num, end=" ")  # Print the prime number
    num += 1
