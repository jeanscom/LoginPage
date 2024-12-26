
# (a) Write a python program to find the maximum of 2 numbers. Take input from keyboard.
# Display the maximum number with appropriate message.
# (b) Modify the above program to find the maximum of 3 numbers

# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Compare and find the maximum
if num1 >= num2 and num1 >= num3:
    print(f"The maximum number is {num1}.")
elif num2 >= num1 and num2 >= num3:
    print(f"The maximum number is {num2}.")
else:
    print(f"The maximum number is {num3}.")
