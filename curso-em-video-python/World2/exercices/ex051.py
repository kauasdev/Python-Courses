first_num = int(input("Enter the first number: "))
reason = int(input("Enter the reason: "))

count = 0

tenth_num = first_num + (10 - 1) * reason

for num in range(first_num, tenth_num + reason, reason):
    print(f"{num} --> ", end='')
