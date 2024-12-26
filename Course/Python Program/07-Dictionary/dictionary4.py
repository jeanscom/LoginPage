# Create a nested dictionary to store details of multiple students, with each student's details (name, age, and marks) being another dictionary.
# Initialize the nested dictionary
students = {
    "student1": {"name": "Alice", "age": 20, "marks": 85},
    "student2": {"name": "Bob", "age": 22, "marks": 90},
    "student3": {"name": "Charlie", "age": 19, "marks": 78}
}

# Print the nested dictionary
for key, value in students.items():
    print(f"{key}: {value}")
