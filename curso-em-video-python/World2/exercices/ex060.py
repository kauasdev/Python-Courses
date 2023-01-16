mult = num = int(input("Enter the number: "))
c = 1

while num != 2:
    if c == 1:
        print(f"{num}! = {num}x", end='')
        c += 1
    else:
        num -= 1
        print(f"{num}x", end='')
        mult *= num
print(f"1 = {mult}\n\n")