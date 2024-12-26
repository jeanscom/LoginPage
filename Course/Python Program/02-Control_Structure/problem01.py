
# Write a program to check whether a number is strong number or not.Strong number is a special number whose sum of factorial of digits is equal to the original number.

# Input from the user
number = int(input("Enter a number: "))
original_number = number
sum_of_factorials = 0

# Loop through each digit of the number
while number > 0:
    digit = number % 10  # Get the last digit
    number //= 10        # Remove the last digit

    # Calculate factorial of the digit
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
    
    # Add the factorial of the digit to the sum
    sum_of_factorials += factorial

# Check if the sum of factorials is equal to the original number
if sum_of_factorials == original_number:
    print(f"{original_number} is a Strong number.")
else:
    print(f"{original_number} is not a Strong number.")