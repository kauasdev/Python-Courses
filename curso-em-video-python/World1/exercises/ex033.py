nums = []
for i in range(3):
    nums.append(int(input("Enter the number: ")))

num1, num2, num3 = nums

if num1 < num2 and num1 < num3:
    smallest = num1
if num1 > num2 and num1 > num3:
    biggest = num1

if num2 < num1 and num2 < num3:
    smallest = num2
if num2 > num1 and num2 > num3:
    biggest = num2

if num3 < num2 and num3 < num1:
    smallest = num3
if num3 > num2 and num3 > num1:
    biggest = num3

print(f"\n{smallest} is the smallest number")
print(f"{biggest} is the biggest number")