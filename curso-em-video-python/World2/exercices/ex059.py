action = 0
while True:
    if action != 4:
        print("=-="*16)
        num1 = float(input("Enter the number: "))
        num2 = float(input("Enter the number: "))

    action = int(input("""\nChoose an action:
    [1] Add
    [2] Multiply
    [3] Higher
    [4] New numbers
    [5] Exit

    ----> """))

    if action == 1:
        print(f"\nThe sum between {num1} and {num2} is {num1 + num2}")
    elif action == 2:
        print(f"\nThe multiplication between {num1} and {num2} is {num1 * num2}")
    elif action == 3:
        if num1 > num2:
            print(f"\n{num1} is greater than {num2}")
        elif num2 > num1:
            print(f"\n{num2} is greater than {num1}")
    elif action == 4:
        num1 = float(input("Enter the number: "))
        num2 = float(input("Enter the number: "))
    elif action == 5:
        print("\nFinish.")
        break
    else:
        print("Invalid option!!")
