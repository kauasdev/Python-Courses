sorted_nums = []

for i in range(0, 5):
    num = int(input("Enter the number: "))
    
    if i == 0 or num > sorted_nums[-1]:
        sorted_nums.append(num)
    else:
        for i, n in enumerate(sorted_nums):
            if num <= n:
                sorted_nums.insert(i, num)
                break

print(f"The numbers entered were {sorted_nums}")
