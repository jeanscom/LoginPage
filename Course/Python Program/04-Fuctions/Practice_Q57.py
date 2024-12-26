#Write a Python function that prints out the first n rows of Pascal&#39;s triangle.
def print_pascals_triangle(n):
    if n <= 0:
        print("Number of rows must be a positive integer.")
        return
    
    # Initialize the first row
    triangle = [[1]]
    
    # Generate rows
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # First element is always 1
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])  # Sum of adjacent elements
        new_row.append(1)  # Last element is always 1
        triangle.append(new_row)
    
    # Print the triangle
    for row in triangle:
        print(' '.join(map(str, row)).center(2 * n))

# Example usage
print_pascals_triangle(5)
