# Write a program to compute nth fibonaccii number using recursion

def fibonacci(n):
    # Base case: the first two Fibonacci numbers are 0 and 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: sum of the two preceding numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    # Input from the user
    n = int(input("Enter the position n to find the nth Fibonacci number: "))
    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        result = fibonacci(n)
        print(f"The {n}th Fibonacci number is: {result}")

if __name__ == "__main__":
    main()