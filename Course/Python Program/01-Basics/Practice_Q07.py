#Python Program to Calculate the Area and Perimeter of Triangles and Circles.
import math

def calculate_triangle():
    print("\n--- Triangle ---")
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))
    
    # Calculate perimeter
    perimeter = a + b + c
    print(f"Perimeter of the triangle: {perimeter}")
    
    # Calculate area using Heron's formula
    s = perimeter / 2  # semi-perimeter
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Area of the triangle: {area}")

def calculate_circle():
    print("\n--- Circle ---")
    radius = float(input("Enter the radius: "))
    
    # Calculate area
    area = math.pi * radius**2
    print(f"Area of the circle: {area}")
    
    # Calculate circumference (perimeter)
    circumference = 2 * math.pi * radius
    print(f"Circumference of the circle: {circumference}")

# Main Program
print("Choose the shape to calculate:")
print("1. Triangle")
print("2. Circle")
choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    calculate_triangle()
elif choice == 2:
    calculate_circle()
else:
    print("Invalid choice. Please choose 1 or 2.")
