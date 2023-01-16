from datetime import date

of_age = 0
minor = 0

current_year = date.today().year

for person in range(1, 7):
    year_birth = int(input("Enter the year of birth: "))

    if current_year - year_birth >= 21:
        of_age += 1
    else:
        minor += 1

print(f"{of_age} people of legal age")
print(f"{minor} underage people")