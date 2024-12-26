#Program to define a module to find Fibonacci Numbers and import the module to another program.

# Import the fibonacci module
import Q6_1

# Input to get the Fibonacci number or sequence
n = int(input("Enter the value of n to get the nth Fibonacci number or sequence: "))

# Get the nth Fibonacci number
print(f"The {n}th Fibonacci number is: {Q6_1.fibonacci(n)}")

# Get the Fibonacci sequence up to the nth term
print(f"The Fibonacci sequence up to {n} terms is: {Q6_1.fibonacci_sequence(n)}")
