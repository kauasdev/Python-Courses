sum = 0

for num in range(1, 501):
    if num % 2 != 0:
        if num % 3 == 0:
            sum += num
        else:
            pass
    else:
        pass

print(f"The sum of all odd numbers divisible by 3 between 1 and 500 is {sum}")
