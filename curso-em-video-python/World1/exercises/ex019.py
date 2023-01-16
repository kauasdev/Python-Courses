from random import randint, choice

students = []

for i in range(4):
    student = input("Enter the student name: ")
    students.append(student)

# num = randint(1, 4)
# student_draw = students[num]

student_chosen = choice(students)

print('\nThe student chosen was {}'.format(student_chosen))
