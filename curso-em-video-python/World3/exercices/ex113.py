num_int = num_float = 0

while True:
    try:
        num_int = int(input("Enter an integer: "))
    except (ValueError, TypeError):
        print("Error! Enter a valid integer!")
    except Exception as error:
        print(f"{error.__class__}")
    else:
        break

while True:
    try:
        num_float = float(input("Enter a floating number: "))
    except (ValueError, TypeError):
        print("Error! Enter a valid floating number!")
    except Exception as error:
        print(f"{error.__class__}")
    else:
        break

print(f"\nInteger: {num_int}\nFloating number: {num_float}")
