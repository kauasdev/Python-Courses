nums = []
smallest_num = biggest_num = 0

for i in range(0, 5):
    num = float(input("Enter the number: "))
    nums.append(num)

    if num > biggest_num:
        biggest_num = num
    elif num < smallest_num or smallest_num == 0:
        smallest_num = num

print(f"\nThe smallest number is {smallest_num} and it is in position ", end='')
for i, v in enumerate(nums):
    if v == smallest_num:
        print(f"{i}, ", end='')
print("\n")
print(f"The biggest number is {biggest_num} and it is in position ", end='')
for i, v in enumerate(nums):
    if v == biggest_num:
        print(f"{i}, ", end='')
print("\n")
