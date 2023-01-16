num = int(input("Enter the number: "))
total_num = 0
sum = 0

while num != 999:
    total_num += 1
    sum += num

    num = int(input("Enter the number: "))

print(f"You entered {total_num} numbers, and the sum between them is {sum}")