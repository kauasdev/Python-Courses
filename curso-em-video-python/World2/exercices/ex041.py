from datetime import date

year_of_birth = int(input("Enter the athlete's year of birth: "))
current_year = date.today().year

if year_of_birth > current_year:
    print("Invalid year!")
    quit()

age = current_year - year_of_birth

if age <= 9:
    print("Little")
elif age <= 14:
    print("Children")
elif age <= 19:
    print("Junior")
elif age == 20:
    print("Senior")
else:
    print("Master")