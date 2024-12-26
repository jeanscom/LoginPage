
# Write a python program to take two integers from the user as input and
# print all integers between them using (a) for loop (b) while loop.

# Taking two integers as input
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# (a) Using a for loop to print all integers between num1 and num2
print("Using for loop:")
if num1 < num2:
    for i in range(num1 + 1, num2):
        print(i)
else:
    for i in range(num2 + 1, num1):
        print(i)

# (b) Using a while loop to print all integers between num1 and num2
print("\nUsing while loop:")
if num1 < num2:
    i = num1 + 1
    while i < num2:
        print(i)
        i += 1
else:
    i = num2 + 1
    while i < num1:
        print(i)
        i += 1
