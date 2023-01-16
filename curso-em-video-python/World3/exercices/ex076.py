products_tuple = ("Juice", 1, "Cake", 5, "Potato", 7,
                  "Candy", 0.5, "Egg", 0.5, "Meat", 10)
print('='*40)
print(f"{' PRICES ':^40}")
print('='*40)

name = ''
price = 0

for i, value in enumerate(products_tuple):
    if type(value) == str:
        name = value
        price = products_tuple[i+1]
        dots = 40 - len(name) - 6
        print(f"{name:.<30}R$ {price:.2f}")
print('='*40)
