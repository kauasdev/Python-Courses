number = int(input("Enter number: "))

print('-'*20)
for i in range(11):
    print('{} x {:2} = {}'.format(number, i, number * i))
print('-'*20)
