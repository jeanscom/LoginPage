# Python Program to Solve Quadratic Equation
import cmath  # Use cmath to handle complex roots

def solve_quadratic(a, b, c):
    if a == 0:
        print("This is not a quadratic equation (a cannot be 0).")
        return
    
    # Calculate the discriminant
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    
    # Calculate the two solutions
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)
    
    print(f"The solutions are: {root1} and {root2}")

# Input coefficients
print("Solve the quadratic equation ax^2 + bx + c = 0")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Solve the quadratic equation
solve_quadratic(a, b, c)
