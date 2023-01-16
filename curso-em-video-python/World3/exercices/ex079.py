values = list()

while True:
    res = "S"
    num = float(input("\nEnter the coin: "))
    if num in values:
        res = input("Do you wish to continue(Y/N): ").strip().upper()
    else:
        values.append(num)
        res = input("Do you wish to continue(Y/N): ").strip().upper()
    
    if res in "YN":
        if res == "N":
            break
    else:
        print("\nInvalid answer!! Try again!")
        res = input("Do you wish to continue(Y/N): ").strip().upper()

print(f"\nThe numbers entered were {sorted(values)}")
