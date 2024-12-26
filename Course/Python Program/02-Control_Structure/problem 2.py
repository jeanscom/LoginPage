
# Write a program to read an integer x as input and print the digits from right to left order
# (that is LSB to MSB), on separate lines.
# Input: an integer
x = int(input("Enter an integer: "))

# Process each digit from right to left
while x > 0:
    # Extract the least significant digit (LSB)
    digit = x % 10
    # Print the digit
    print(digit)
    # Remove the least significant digit from x
    x = x // 10
