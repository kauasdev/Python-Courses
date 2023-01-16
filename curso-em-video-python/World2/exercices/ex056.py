age_sum = 0
older_man_name = ''
older_man_age = 0
women_under_20 = 0

for person in range(1, 5):
    print('='*25)
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    sex = input("Enter the sex (M/W): ").upper()

    age_sum += age

    if sex == "M" or sex == "W":
        if sex == "M" and age > older_man_age:
            older_man_age = age
            older_man_name = name
        if sex == "W" and age < 20:
            women_under_20 += 1

average_age = age_sum / 4

print(f"\n{'='*35}")
print(f"The average age of the group is {average_age} years")
print(f"{older_man_name} is the oldest man")
print(f"{women_under_20} women under 20 years old")
print('='*35)