from random import randint, choice, shuffle

students = []
# students_order = []
for i in range(4):
    student = input("Enter the student name: ")
    students.append(student)

# for i in range(0, len(students)):
#     # num = randint(0, len(students) - 1)
#     # student_chosen = students[num]

#     student_chosen = choice(students)
#     students_order.append(student_chosen)
#     students.remove(student_chosen)

print('\n')
# for i in range(0, len(students_order)):
#     print('Student {}° -> {}'.format(i+1, students_order[i]))

shuffle(students)
for i in range(0, len(students)):
    print('Student {}° -> {}'.format(i+1, students[i]))