people = list()
person = list()

greater_weight = less_weight = 0

while True:
    res = "S"

    person = [input("\nName: "), float(input("Weight: "))]
    people.append(person[:])

    res = input("Do you wish to continue[Y/N]: ").strip().upper()
    if res in "YN":
        if res == "N":
            break
    else:
        break

for i, p in enumerate(people):
    if i == 0:
        greater_weight = less_weight = p[1]
    elif p[1] < less_weight:
        less_weight = p[1]
    elif p[1] > greater_weight:
        greater_weight = p[1]

print(f"{len(people)} people were registered")
print(f"The heaviest weight was {greater_weight} Kg. Weight of ", end='')
for p in people:
    if p[1] == greater_weight:
        print(f"[{p[0]}], ", end='')
print(f"\nThe lowest weight was {less_weight} Kg. Weight of ", end='')
for p in people:
    if p[1] == less_weight:
        print(f"[{p[0]}], ", end='')
print("\n")
