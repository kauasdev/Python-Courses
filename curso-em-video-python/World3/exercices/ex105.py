def average_grades(grade):
    total = 0
    print(grade)
    for g in grade:
        total += g
    return total / len(grade)


def check_situation(grade):
    if grade < 6:
        return "Recovery"
    else:
        return "Approved"


def grades(*args):
    sit = args[1]
    grades_dict = dict()
    grades_dict["total"] = len(args[0])
    grades_dict["highest_grade"] = max(args[0])
    grades_dict["lowest_grade"] = min(args[0])
    grades_dict["average"] = average_grades(args[0])

    if sit:
        grades_dict["situation"] = check_situation(grades_dict["average"])

    return grades_dict


student = grades((4, 8, 6, 9), True)
print(student)
