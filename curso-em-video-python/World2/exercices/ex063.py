print(f"{'='*8} Fabonacci sequence {'='*8}")
num = int(input("Enter the number: "))

c = 0
fibonacci_num = 0
num1 = 0
num2 = 0

while c < num:
    if c == 0:
        print("0 -> ", end='')
        num1 = c
        c += 1
    elif c == 1:
        print("1 -> ", end='')
        num2 = c
        c += 1
    else:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        if c == num - 1:
            print(f"{num3}")
        else:
            print(f"{num3} -> ", end='')
        c += 1

