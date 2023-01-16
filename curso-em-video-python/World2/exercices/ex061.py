first_num = int(input("Enter the first number: "))
reason = int(input("Enter the reason: "))

count = 1

while count < 11:
    print(f"{first_num} --> ", end='')
    first_num += reason
    count += 1
 