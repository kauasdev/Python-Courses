student = dict()

student["name"] = input("Name: ")
student["average"] = float(input("What is the student's average: "))

if student["average"] <= 5.9:
    student["situation"] = "Disapproved"
else:
    student["situation"] = "Approved"

print("="*20)
for k, v in student.items():
    print(f"{k.title()}: {v}")
    