sum = 0

for num in range(1, 7):
    num = float(input("Enter the number: "))
    
    if num % 2 == 0:
        sum += num
    else:
        pass

print(f"The sum of the even numbers is {sum}")
