import coin

num = float(input("Enter the price: "))
print(f"Half: {coin.half(num)}")
print(f"Double: {coin.double(num)}")
print(f"Increasing 13%: {coin.increase(num, 13)}")
print(f"Reducing 22%: {coin.reduction(num, 22)}")
