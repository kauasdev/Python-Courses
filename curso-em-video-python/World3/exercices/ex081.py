nums = list()

while True:
    res = "S"

    num = int(input("Enter the number: "))
    nums.append(num)

    res = input("Do you wish to continue(Y/N): ").strip().upper()

    if res in "YN":
        if res == "N":
            break
        else:
            continue
    else:
        break

print(f"\n{len(nums)} numbers were entered.")
print(sorted(nums, reverse=True))
if 5 in nums:
    print("The number 5 was typed in the list")
else:
    print("The number 5 wasn't typed in the list")