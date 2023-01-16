grade1 = float(input("Enter student grade: "))
grade2 = float(input("Enter student grade: "))

student_average = (grade1 + grade2) / 2

if student_average <= 5:
    print("Disapproved")
elif student_average > 5 and student_average <= 6.9:
    print("Recovery")
elif student_average >= 7:
    print("Approved")
