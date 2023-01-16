from datetime import date
year = int(input("Enter the year, or enter 0 to check the current year: "))

if year == 0:
    year = date.today().year
if year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} isn't a leap year")