# Write a Python program that calculates and prints the sum of squares of all possible pairs of two distinct integers from a given range [start, end] including start and end values


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

sum_of_squares = 0

# Iterate over each pair of distinct integers in the range
for i in range(start, end + 1):
    for j in range(start, end + 1):
        # Skip if i and j are the same
        if i == j:
            continue
        # Calculate the sum of squares of the pair
        sum_of_squares += i ** 2 + j ** 2

print("Sum of squares of all possible pairs of two distinct integers in the range [{} , {}] is: {}".format(start, end, sum_of_squares))