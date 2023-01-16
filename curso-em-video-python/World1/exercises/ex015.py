days = int(input("How many days rented: "))
km = float(input("How many KM run: "))

price = (days * 60) + (km * 0.15)

print('\n{}\n Days: {}\n Km: {}\n Price: {} \n{}'.format(('='*20), days, km, price, ('='*20)))