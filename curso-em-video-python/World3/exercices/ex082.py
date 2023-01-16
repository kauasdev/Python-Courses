all_nums = []
even_nums = []
odd_nums = []

while True:
    res = "S"

    num = int(input("Enter the number: "))
    all_nums.append(num)
    res = input("Do you wish to continue(Y/N): ").strip().upper()
    
    if res in "YN":
        if res == "N":
            break
    else:
        break

for num in all_nums:
    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num)

print(f"\nAll numbers: {all_nums}")
print(f"Even numbers: {even_nums}")
print(f"Odd numbers: {odd_nums}")