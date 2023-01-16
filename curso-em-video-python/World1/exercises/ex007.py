grade_one = float(input("Enter the student's first grade: "))
grade_two = float(input("Enter the student's second grade: "))

student_average = (grade_one + grade_two) / 2

print('Student grades: {:.2f} - {:.2f}'.format(grade_one, grade_two))
print('Student average: {}'.format(student_average))