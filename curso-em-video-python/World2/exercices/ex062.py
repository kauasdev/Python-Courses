first_num = int(input("Enter the first number: "))
reason = int(input("Enter the reason: "))

count = 0

while count < 10:
    print(f"{first_num} --> ", end='')
    first_num += reason
    count += 1

more_num = int(input("\nHow many more numbers do you want to see: "))

while more_num != 0:
    current_count = count
    while count != current_count + more_num:
        print(f"{first_num} --> ", end='')
        first_num += reason
        count += 1
        
    more_num = int(input("\nHow many more numbers do you want to see: "))
