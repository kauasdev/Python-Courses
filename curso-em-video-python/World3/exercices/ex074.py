from random import randint

higher_num = 0
smallest_num = num1 = randint(0, 100)
num2 = randint(0, 100)
num3 = randint(0, 100)
num4 = randint(0, 100)
num5 = randint(0, 100)

tuple = (num1, num2, num3, num4, num5)

print(tuple)

# for num in tuple:
#     if num < smallest_num:
#         smallest_num = num
#     elif num > higher_num:
#         higher_num = num
higher_num = max(tuple)
smallest_num = min(tuple)

print(f"\nThe biggest number is {higher_num}")
print(f"The smallest number is {smallest_num}")