#Write a Python program to print the Fibonacci series up to n terms.
# Input the number of terms
n = int(input("Enter the number of terms: "))

# Initialize the first two terms of the Fibonacci series
a, b = 0, 1

# Print the Fibonacci series up to n terms
print("Fibonacci series up to", n, "terms:")
for _ in range(n):
    print(a, end=" ")  # Print the current term
    a, b = b, a + b  # Update a and b to the next two terms
