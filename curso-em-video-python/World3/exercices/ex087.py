matrix = [[], [], []]
even_num = []

for i in range(0, 3):
    for n in range(0, 3):
        value = int(input(f"Enter a value for [{i}, {n}]: "))
        if value % 2 == 0:
            even_num.append(value)

        if i == 0:
            matrix[0].append(value)
        elif i == 1:
            matrix[1].append(value)
        elif i == 2:
            matrix[2].append(value)

print(f"\n{'='*20}\n")
for row in matrix:
    for i, v in enumerate(row):
        if i == len(row) - 1:
            print(f"[ {v} ]")
        else:
            print(f"[ {v} ]", end='')
print(f"\n{'='*20}\n")
sum_of_third_col = matrix[0][2] + matrix[1][2] + matrix[2][2]

print(f"The sum of the even numbers is {sum(even_num)}")
print(f"The sum of the numbers in the third column is {sum_of_third_col}")
print(f"The largest number in the second row is {max(matrix[1])}")
