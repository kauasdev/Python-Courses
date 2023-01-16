# test = False

# while True:
#     infinite loop
#     if test:
#         print("Code")
#     else:
#         break
#         stop loop
num = sum = 0

while True: # (num != 999) -> Flag
    num = float(input("Enter a number: "))

    if num == 999:
        break

    sum += num

print(f"The sum of the values is {sum:.2f}")
