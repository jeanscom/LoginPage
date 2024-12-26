# Program that accepts the lengths of three sides of a triangle as inputs. The program output should indicate whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides). Implement using functions.
# Function to check if the triangle is a right triangle
def is_right_triangle(a, b, c):
    # Sort the sides to ensure that the largest side is treated as the hypotenuse
    sides = sorted([a, b, c])
    
    # Check if the Pythagorean Theorem holds: a^2 + b^2 = c^2
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

# Function to get input from the user
def get_triangle_sides():
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))
    return a, b, c

# Main function
def main():
    # Get the sides of the triangle from the user
    a, b, c = get_triangle_sides()
    
    # Check if the triangle is a right triangle
    if is_right_triangle(a, b, c):
        print(f"The triangle with sides {a}, {b}, and {c} is a right triangle.")
    else:
        print(f"The triangle with sides {a}, {b}, and {c} is not a right triangle.")

# Call the main function to execute the program
main()
    