# Create a nested dictionary to store details of a class, where each key represents a student ID, and the value is a dictionary containing their name, age, and grade. Access the name and grade of a specific student by their ID.
# Initialize the nested dictionary
class_details = {
    101: {"name": "Alice", "age": 20, "grade": "A"},
    102: {"name": "Bob", "age": 22, "grade": "B"},
    103: {"name": "Charlie", "age": 19, "grade": "A-"},
}

# Access details of a specific student by ID
student_id = int(input("Enter the student ID: "))

if student_id in class_details:
    name = class_details[student_id]["name"]
    grade = class_details[student_id]["grade"]
    print(f"Student Name: {name}")
    print(f"Grade: {grade}")
else:
    print("Student ID not found.")
