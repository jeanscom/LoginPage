
# Write a python program to check if a number given by the user is a
# palindrome. (Hint: A number is a palindrome if the number is equal to its
# reverse.)

# Taking input from the user
num = int(input("Enter a number: "))

# Converting the number to a string to easily reverse it
num_str = str(num)

# Reversing the string and checking if it's equal to the original number
if num_str == num_str[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

