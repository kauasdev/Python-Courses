name = input("What is your name: ")
print('!{:20}!'.format(name))
print('!{:>20}!'.format(name))
print('!{:<20}!'.format(name))
print('!{:^20}!'.format(name))
print('!{:=^20}!'.format(name))

# !kaua                !
# !                kaua!
# !kaua                !
# !        kaua        !
# !========kaua========!

n1 = int(input("\nWrite a number: "))
n2 = int(input("Write a number: "))

sum = n1 + n2
mul = n1 * n2
div = n1 / n2
i_div = n1 // n2
rest = n1 % n2
pot = n1 ** n2

print('\n Sum: {} \n Product: {} \n Division: {:.2f} \n Integer Division: {} \n Rest of Division: {} \n Potency: {}'.format(sum, mul, div, i_div, rest, pot))
