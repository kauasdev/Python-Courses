from random import randint

accuracy = 0
while True:
    print(f"{'='*18}\n")
    num = int(input("Enter the number: "))
    choice = input("Even or odd (E/O): ").upper()
    if choice not in "EO":
        print("Invalid! Try again...")
        choice = input("Even or odd (E/O): ").upper()
    else:
        pc_num = randint(0, 9999)
        total = num + pc_num

        if total % 2 == 0 and choice == "E":
            print(f"The computer chose {pc_num}")
            print(f"\nThe number {total} is Even. You win!!")
            accuracy += 1
        elif total % 2 != 0 and choice == "O":
            print(f"The computer chose {pc_num}")
            print(f"\nThe number {total} is Odd. You win!!")
            accuracy += 1
        else:
            print(f"\nYou lost wit {accuracy} hits!")
            print(f"\n{'='*18}")
            break
    print(f"\n{'='*18}")



