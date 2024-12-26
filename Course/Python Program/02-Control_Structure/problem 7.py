
# Write a Python program that prints all the numbers from 0 to 100 except multiples of 3 or 5.
# Loop through numbers from 0 to 100
for num in range(101):
    if num % 3 != 0 and num % 5 != 0:  # Check if the number is not a multiple of 3 or 5
        print(num)
