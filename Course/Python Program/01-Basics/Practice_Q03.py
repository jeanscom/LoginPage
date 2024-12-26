#Write a Python program to get the Python version you are using
# Accept an integer input from the user
n = int(input("Enter an integer (n): "))

# Compute the value of n + nn + nnn
result = n + int(f"{n}{n}") + int(f"{n}{n}{n}")

# Display the result
print(f"The computed value of n + nn + nnn is: {result}")
