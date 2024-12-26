# Write a function to read a matrix and display the matrix. You are
# given a matrix and find the following. Use functions for each task. Pass input to 
# each task as parameters and return the result. 
# (a) Sum of the elements in each row
# (b) sum of the elements in each column
# (c) Trace of the matrix
# (d) Is it a symmetric matrix?
# (e) Add 2 matrices

def read_matrix(rows, cols):
    """Reads a matrix from user input."""
    matrix = []
    print("Enter the elements of the matrix row by row:")
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != cols:
            print(f"Please enter exactly {cols} elements.")
            return None
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    """Displays the matrix."""
    for row in matrix:
        print(" ".join(map(str, row)))

def sum_of_rows(matrix):
    """Returns the sum of elements in each row."""
    return [sum(row) for row in matrix]

def sum_of_columns(matrix):
    """Returns the sum of elements in each column."""
    return [sum(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))]

def trace_of_matrix(matrix):
    """Returns the trace of the matrix."""
    if len(matrix) != len(matrix[0]):
        raise ValueError("Trace can only be calculated for square matrices.")
    return sum(matrix[i][i] for i in range(len(matrix)))

def is_symmetric(matrix):
    """Checks if the matrix is symmetric."""
    rows = len(matrix)
    cols = len(matrix[0])
    if rows != cols:
        return False
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def add_matrices(matrix1, matrix2):
    """Adds two matrices."""
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions to be added.")
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

# Example usage
if __name__ == "__main__":
    # Read matrix dimensions
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    # Read and display the first matrix
    matrix1 = read_matrix(rows, cols)
    if matrix1 is None:
        exit()
    print("Matrix 1:")
    display_matrix(matrix1)

    # Read and display the second matrix
    matrix2 = read_matrix(rows, cols)
    if matrix2 is None:
        exit()
    print("Matrix 2:")
    display_matrix(matrix2)

    # Sum of elements in each row
    print("Sum of elements in each row:", sum_of_rows(matrix1))

    # Sum of elements in each column
    print("Sum of elements in each column:", sum_of_columns(matrix1))

    # Trace of the matrix
    try:
        print("Trace of the matrix:", trace_of_matrix(matrix1))
    except ValueError as e:
        print(e)

    # Check if the matrix is symmetric
    print("Is the matrix symmetric?", is_symmetric(matrix1))

    # Add two matrices
    try:
        result_matrix = add_matrices(matrix1, matrix2)
        print("Result of adding the two matrices:")
        display_matrix(result_matrix)
    except ValueError as e:
        print(e)