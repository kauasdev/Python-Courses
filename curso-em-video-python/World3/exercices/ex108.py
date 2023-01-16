import coin

num = float(input("Enter the price: R$"))

print(f"Price: {coin.coin(num)}")
print(f"Half: {coin.coin(coin.half(num))}")
print(f"Double: {coin.coin(coin.double(num))}")
print(f"Increasing 13%: {coin.coin(coin.increase(num, 13))}")
print(f"Reducing 22%: {coin.coin(coin.reduction(num, 22))}")
