want_continue = "Y"
average = 0
bigger = 0
smaller = 0

c = 0
sum = 0

while want_continue == "Y":
    num = int(input("Enter the number: "))
    smaller = num
    if num > bigger:
        bigger = num
    if num < smaller:
        smaller = num
    
    sum += num
    c += 1

    want_continue = input("Do you want to continue? (Y/N): ").upper()

print(f"Bigger number: {bigger}")
print(f"Smaller number: {smaller}")
print(f"The average of these numbers is {sum/c}")