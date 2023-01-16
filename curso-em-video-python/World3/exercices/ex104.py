def is_int(v):
    if v.isnumeric():
        return True
    else:
        return False


while True:
    n = input("Enter the number: ")
    if is_int(n):
        break
    else:
        print("ERROR!! Enter the valid integer")
