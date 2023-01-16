from math import floor

count = sum = 0

while True:
    num = float(input("Enter the number (999 to stop): "))
    if floor(num) == 999:
        break
    else:
        sum += num
        count += 1

print(f"You entered {count} numbers and the sum between them is {sum:.2f}")