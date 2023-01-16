from datetime import date

year = int(input("Enter your year of birth: "))
current_year = date.today().year
age = current_year - year

if age < 18:
    print(f"You don't need to enlist now.{18 - age} years to go.")
elif age == 18:
    print("You need to enlist now")
else:
    print(f"You should have signed up. Spent {age -18} years")