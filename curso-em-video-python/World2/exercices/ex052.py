num = int(input("Enter the number: "))

mult = 0

for i in range(1, num+1):
    if num % i == 0:
        mult += 1
    else:
        pass

if mult == 2:
    print(f"Number {num} is prime")
else:
    print(f"Number {num} isn't prime")