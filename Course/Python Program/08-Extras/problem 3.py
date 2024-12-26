
# Write a program that takes a 3-digit number as input and prints its reverse. For example,
# if the input is 345 then the output is 543. Given that none of the digits is a 0.

# Input: A 3-digit number
x = int(input("Enter a 3-digit number: "))

# Reverse the number
reverse_x = (x % 10) * 100 + ((x // 10) % 10) * 10 + (x // 100)

# Output the reversed number
print("The reverse of the number is:", reverse_x)
