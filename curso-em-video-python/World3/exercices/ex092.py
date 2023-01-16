from datetime import date

person = dict()

person['name'] = input("What's your name: ")
person['year_birth'] = int(input("What year were you born: "))
person['work_card'] = int(input("Work card (0 doesn't have): "))

if person['work_card']:
    person['year_of_hire'] = int(input("Year of hire: "))
    person['salary'] = float(input("Salary: $"))
    retirement = person['year_of_hire'] + 35
    retirement_age = retirement - person['year_birth']
    person['retirement_age'] = retirement_age

print("="*25)
for k, v in person.items():
    k = " ".join(str(k).split("_")).title()
    print(f"{k}: {v}")
