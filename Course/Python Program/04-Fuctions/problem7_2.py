# Write a program to print the digits in a given number in the order MSD to LSD
# using recursion.

def print_digits(n):
    # Base case: if n is 0, return
    if n == 0:
        return
    else:
        # Recursive call with the number divided by 10 (removing the last digit)
        print_digits(n // 10)
        # Print the last digit
        print(n % 10, end=' ')

def main():
    # Input from the user
    number = int(input("Enter a number: "))
    
    # Handle the case when the number is 0
    if number == 0:
        print("Digits in order (MSD to LSD): 0")
    else:
        print("Digits in order (MSD to LSD):", end=' ')
        print_digits(number)
        print()  # For a new line after printing the digits

if __name__ == "__main__":
    main()	