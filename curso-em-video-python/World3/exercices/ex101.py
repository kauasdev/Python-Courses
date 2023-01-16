from datetime import date


def check_vote(year_birth):
    age = date.today().year - year_birth
    if 16 <= age < 18 or age > 70:
        print(f"At {age} years old, voting is optional")
    elif 18 <= age <= 70:
        print(f"At the age of {age}, voting is mandatory")
    else:
        print("Vote denied")


year = int(input("What year were you born: "))
check_vote(year)
