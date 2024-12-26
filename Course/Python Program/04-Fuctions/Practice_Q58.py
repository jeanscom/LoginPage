#  Write a Python function to create and print a list where the values are squares of numbers
# between 1 and 30 (both included).

def generate_square_list():
    # Generate the list of squares using a list comprehension
    squares = [x**2 for x in range(1, 31)]
    # Print the resulting list
    print("List of squares:", squares)

# Call the function
generate_square_list()
