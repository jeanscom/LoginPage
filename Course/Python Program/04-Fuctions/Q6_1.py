#Program to define a module to find Fibonacci Numbers and import the module to another program.

# Function to calculate the nth Fibonacci number
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Function to generate a list of Fibonacci numbers up to nth term
def fibonacci_sequence(n):
    if n <= 0:
        return "Input should be a positive integer"
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
