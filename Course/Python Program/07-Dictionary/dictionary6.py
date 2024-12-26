# Create a nested dictionary where each key is a student's name, and the value is a list of their marks in 3 subjects. Calculate and display each student's average marks.
# Initialize the nested dictionary
students = {
    "Alice": [85, 90, 88],
    "Bob": [78, 81, 74],
    "Charlie": [92, 88, 95]
}

# Calculate and display each student's average marks
for name, marks in students.items():
    average = sum(marks) / len(marks)
    print(f"{name}'s average marks: {average:.2f}")
