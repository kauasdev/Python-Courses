people = list()
women = list()
above_average_age = list()
person = dict()
sum_age = 0

while True:
    person["name"] = input("Name: ")
    person["gender"] = input("Gender[M/W]: ").strip().upper()
    person["age"] = int(input("How old are you: "))

    if person["gender"] not in "MW":
        print("Invalid gender!")
        person["gender"] = input("Gender[M/W]: ").strip().upper()

    people.append(person.copy())

    res = input("Do you wish to continue[Y/N]: ").strip().upper()
    if res in "YN":
        if res == "N":
            break
    else:
        break

for p in people:
    sum_age += p["age"]
    if p["gender"] == "W":
        women.append(p["name"])
    else:
        continue

average_age = sum_age / len(people)

for p in people:
    if p["age"] > average_age:
        above_average_age.append(p["name"])

print("="*30)
print(f"\n{len(people)} were registered.")
print(f"The average age is {average_age}")
print(f"Women: {women}")
print(f"People above average age: {above_average_age}")
