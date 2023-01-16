school = list()

while True:
    name = input("\nName: ")
    grades = [float(input("Grade 1: ")), float(input("Grade 2: "))]

    school.append([name, grades[:]])

    res = input("Do you wish to continue[Y/N]: ").strip().upper()
    if res in "YN":
        if res == "N":
            break
    else:
        break

print(f"\n{'='*30}")
print(f"{'Num':<4} {'NAME':<15} {'Average':<7}")
for i, stu in enumerate(school):
    student_average = sum(stu[1]) / 2
    print(f"{i:<4} {stu[0]:<15} {student_average:<7}")

while True:
    stu_num = int(input("\nShow which student's grades(999 to stop): "))
    if stu_num == 999:
        break
    else:
        print(f"\n{school[stu_num][0]}'s notes are {school[stu_num][1]}")
