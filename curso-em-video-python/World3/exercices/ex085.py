numbers = [[], []]

for i in range(0, 8):
    num = int(input("Enter the number: "))
    if num % 2 == 0:
        numbers[0].append(num)
    else:
        numbers[1].append(num)

print(f"\nOrdered odd numbers: {sorted(numbers[1])}")
