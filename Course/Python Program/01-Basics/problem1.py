
# Write a program to read a 3-digit integer x as input and print the digits from left to
# right order (that is MSB to LSB), on separate lines.
# Input: A 3-digit integer
x = int(input("Enter a 3-digit integer: "))

# Extract the digits
hundreds = x // 100            # Most significant digit (MSB)
tens = (x // 10) % 10          # Middle digit
ones = x % 10                  # Least significant digit (LSB)

# Output each digit on a new line
print(hundreds)
print(tens)
print(ones)
