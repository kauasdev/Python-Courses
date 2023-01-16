matrix = [[], [], []]

for i in range(0, 3):
    for n in range(0, 3):
        value = int(input(f"Enter a value for [{i}, {n}]: "))
        if i == 0:
            matrix[0].append(value)
        elif i == 1:
            matrix[1].append(value)
        elif i == 2:
            matrix[2].append(value)

print("\n")
for row in matrix:
    for i, v in enumerate(row):
        if i == len(row) - 1:
            print(f"[ {v:^5} ]")
        else:
            print(f"[ {v:^5} ]", end='')
