product_price = float(input("Enter the product price: "))
payment_method = int(input("""Payment method:

1 - Cash (cash/check)
2 - Cash (card)
3 - 2x on the card
4 - 3x on the card

-----> """))
price = 0
if payment_method == 1: 
    price = product_price - (product_price * 0.1)
elif payment_method == 2:
    price = product_price - (product_price * 0.05)
elif payment_method == 3:
    price = product_price
elif payment_method == 4:
    price = product_price + (product_price * 0.2)
else:
    print("Invalid method")

print(f"Total payable: ${price}")
