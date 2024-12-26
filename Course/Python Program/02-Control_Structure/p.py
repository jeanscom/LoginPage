
# You are responsible for grading the final exam of a computer science class. The grading scale
# is as follows:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60
# Write a Python program that takes a student's exam score as input and determines their
# grade using an if-else ladder. The program should display the grade earned by the student.


# Input: student's exam score
score = float(input("Enter the student's exam score: "))

# Determine the grade using an if-else ladder
if score >= 90 and score <= 100:
    grade = 'A'
elif score >= 80 and score < 90:
    grade = 'B'
elif score >= 70 and score < 80:
    grade = 'C'
elif score >= 60 and score < 70:
    grade = 'D'
elif score < 60 and score >= 0:
    grade = 'F'
else:
    grade = 'Invalid score'

# Output the grade
print(f"The grade earned by the student is: {grade}")
