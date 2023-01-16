num = int(input("Enter the number: "))

while True:
    print(f"\n{'='*6}{ {num} }{'='*6}\n")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print(f"\n{'='*6}{ {num} }{'='*6}\n")
    num = int(input("Enter the number: "))
    if num < 0:
        break
    else:
        continue