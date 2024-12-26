# Write a program to print the digits in a number in the reverse order (LSD to MSD)
# using recursion.

def print_digits_reverse(n):
    # Base case: if n is 0, return
    if n == 0:
        return
    else:
        # Print the last digit
        print(n % 10, end=' ')
        # Recursive call with the number divided by 10 (removing the last digit)
        print_digits_reverse(n // 10)

def main():
    # Input from the user
    number = int(input("Enter a number: "))
    
    # Handle the case when the number is 0
    if number == 0:
        print("Digits in reverse order: 0")
    else:
        print("Digits in reverse order:", end=' ')
        print_digits_reverse(number)
        print()  # For a new line after printing the digits

if __name__ == "__main__":
    main()