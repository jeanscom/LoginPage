
# Write a Python program to print all divisors of a given number n.
		
n = int(input("Enter a positive integer: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Divisors of {n} are:")
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            print(i, end=" ")
            if i != n // i:  # Avoid printing the square root twice
                print(n // i, end=" ")
print()