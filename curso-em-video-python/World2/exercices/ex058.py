from random import randint

tries = 0
pc_num = randint(0, 10)
num = int(input("Enter the number: "))

while pc_num != num:
    tries += 1
    print("Wrong!")
    if pc_num > num:
        print("Most...\n")
    elif pc_num < num:
        print("Less...\n")
    num = int(input("Enter the number: "))

print(f"You needed {tries} tries to get it right.")
