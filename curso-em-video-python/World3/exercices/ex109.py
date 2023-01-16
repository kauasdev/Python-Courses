import coin

num = float(input("Enter the price: R$"))

print(f"Half: {coin.half(num, format_price=True)}")
print(f"Double: {coin.double(num, True)}")
print(f"Increasing 13%: {coin.increase(num, 13, format_price=True)}")
print(f"Reducing 22%: {coin.reduction(num, 22, True)}")
