#Write a Python program to check whether a number is Armstrong number or Strong or Prime
# Number of Perfect number or magic number or not
# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to check if a number is an Armstrong number
def is_armstrong(num):
    digits = str(num)
    sum_of_powers = sum(int(digit) ** len(digits) for digit in digits)
    return sum_of_powers == num

# Function to check if a number is a Strong number
def is_strong(num):
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    
    sum_of_factorials = sum(factorial(int(digit)) for digit in str(num))
    return sum_of_factorials == num

# Function to check if a number is a Perfect number
def is_perfect(num):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

# Function to check if a number is a Magic number
def is_magic(num):
    def sum_digits(n):
        return sum(int(digit) for digit in str(n))
    
    while num >= 10:
        num = sum_digits(num)
    
    return num == 1

# Input a number from the user
num = int(input("Enter a number: "))

# Check and print the results for each condition
if is_prime(num):
    print(f"{num} is a Prime number.")
else:
    print(f"{num} is not a Prime number.")
    
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
    
if is_strong(num):
    print(f"{num} is a Strong number.")
else:
    print(f"{num} is not a Strong number.")
    
if is_perfect(num):
    print(f"{num} is a Perfect number.")
else:
    print(f"{num} is not a Perfect number.")
    
if is_magic(num):
    print(f"{num} is a Magic number.")
else:
    print(f"{num} is not a Magic number.")
