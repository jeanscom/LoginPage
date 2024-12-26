#Write a Python program to find the sum of all odd numbers between 1 to n.
#  Input the value of n
n = int(input("Enter the value of n: "))

# Initialize sum variable and the counter
sum_odd = 0
i = 1  # Start from 1, which is the first odd number

# Using a while loop to go through numbers from 1 to n
while i <= n:
    # If the number is odd, add it to the sum
    if i % 2 != 0:
        sum_odd += i
    # Increment i by 1 to check the next number
    i += 1

# Print the sum of odd numbers
print(f"The sum of all odd numbers between 1 and {n} is: {sum_odd}")
