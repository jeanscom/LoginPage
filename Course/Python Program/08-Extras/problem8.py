
# Write a Python program to print the first k terms in the following sequence.
# −1, 2, −3, 4, . . . (−1)k ∗ k.

# Taking input for the number of terms (k)
k = int(input("Enter the number of terms (k): "))

# Loop to print the first k terms in the sequence
for i in range(1, k + 1):
    term = (-1) ** i * i  # Calculate the term using (-1)^i * i
    print(term)
