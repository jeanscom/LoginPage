#Write a Python program to display all even numbers from 1 to N using recursion

def display_even_numbers(n, current=1):
    # Base case: if current exceeds n, stop the recursion
    if current > n:
        return
    # Check if the current number is even
    if current % 2 == 0:
        print(current)
    # Recursive call with the next number
    display_even_numbers(n, current + 1)

def main():
    # Input from the user
    N = int(input("Enter a number N: "))
    print(f"Even numbers from 1 to {N} are:")
    display_even_numbers(N)

if __name__ == "__main__":
    main()