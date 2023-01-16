people_over_18 = mens = women_below_20 = 0

while True:
    print(f"{'='*26}\n")
    gender = input("What's your sex? (M/W): ").strip().upper()
    age = int(input("How old are you: "))

    if age > 18:
        people_over_18 += 1
    if gender == "M":
        mens += 1
    elif gender == "W" and age < 20:
        women_below_20 += 1

    res = input("Do you wish to continue(Y/N): ").strip().upper()
    print(f"\n{'='*26}")
    if res == "N":
        break
    else:
        continue

print(f"People over 18 years old: {people_over_18}")
print(f"Mens: {mens}")
print(f"Women under 18 years old: {women_below_20}")