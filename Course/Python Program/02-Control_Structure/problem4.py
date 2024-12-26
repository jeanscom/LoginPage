
# Write a Python program to print those numbers which are divisible by 7, between 150 and 270 (both included).

# Using a for loop
print("Numbers divisible by 7 between 150 and 270:")

for num in range(150, 271):  # range goes up to 271 to include 270
    if num % 7 == 0:
        print(num)
