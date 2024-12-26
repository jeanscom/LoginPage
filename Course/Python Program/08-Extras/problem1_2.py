# Using dictionary, Implement a Student Database Management System in Python. The
# system should allow users to perform operations such as adding students, updating
# marks, retrieving student details, and displaying all students in the database.
# Students have the flexibility to enroll in a varying number of distinct courses..
# Implement the below dictionary structure and have the below functionalities.Make it 
# Menu driven.
# Add Student: Implement a function add_student(database) that takes student details
# such as name, roll number, subjects, and marks. Add this student to the database.
# Update Marks: Implement a function update_marks(database) that allows the user
# to update the marks for a specific subject of a student identified by their roll number.
# Retrieve Student Details: Implement a function retrieve_student_details(database)
# that retrieves and prints details (name, subjects, and marks) of a student based on
# their roll number.
# Display All Students: Implement a function display_all_students(database) that
# displays details of all students in the database

def add_student(database):
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    subjects = input("Enter subjects (comma-separated): ").split(',')
    marks = {}
    
    for subject in subjects:
        subject = subject.strip()
        mark = float(input(f"Enter marks for {subject}: "))
        marks[subject] = mark
    
    database[roll_number] = {
        'name': name,
        'subjects': marks
    }
    print(f"Student {name} added successfully!\n")


def update_marks(database):
    roll_number = input("Enter roll number of the student: ")
    
    if roll_number in database:
        subject = input("Enter subject to update marks: ")
        if subject in database[roll_number]['subjects']:
            new_mark = float(input(f"Enter new marks for {subject}: "))
            database[roll_number]['subjects'][subject] = new_mark
            print(f"Marks updated successfully for {subject}!\n")
        else:
            print(f"Subject {subject} not found for student {roll_number}.\n")
    else:
        print(f"Student with roll number {roll_number} not found.\n")


def retrieve_student_details(database):
    roll_number = input("Enter roll number of the student: ")
    
    if roll_number in database:
        student = database[roll_number]
        print(f"Name: {student['name']}")
        print("Subjects and Marks:")
        for subject, mark in student['subjects'].items():
            print(f"{subject}: {mark}")
        print()
    else:
        print(f"Student with roll number {roll_number} not found.\n")


def display_all_students(database):
    if not database:
        print("No students in the database.\n")
        return
    
    print("All Students:")
    for roll_number, student in database.items():
        print(f"Roll Number: {roll_number}, Name: {student['name']}")
        print("Subjects and Marks:")
        for subject, mark in student['subjects'].items():
            print(f"{subject}: {mark}")
        print()


def main():
    database = {}
    
    while True:
        print("Student Database Management System")
        print("1. Add Student")
        print("2. Update Marks")
        print("3. Retrieve Student Details")
        print("4. Display All Students")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_student(database)
        elif choice == '2':
            update_marks(database)
        elif choice == '3':
            retrieve_student_details(database)
        elif choice == '4':
            display_all_students(database)
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()