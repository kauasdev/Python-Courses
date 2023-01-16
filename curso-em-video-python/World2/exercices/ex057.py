gender = input("\nWhat's your gender (M/W): ").upper()

while gender not in "MF":
    print("Invalid, try again!")
    gender = input("\nWhat's your gender (M/W): ").upper()

print("Success!")
