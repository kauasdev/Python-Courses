total = products_over_thousand = price_of_cheapest = 0
name_of_cheapest = ''

while True:
    print(f"{'='*32}")
    name = input("What's the product name: ")
    price = float(input("What's the product  price: $"))

    total += price

    if price_of_cheapest == 0 or price < price_of_cheapest:
        price_of_cheapest = price
        name_of_cheapest = name
    
    if price > 1000:
        products_over_thousand += 1

    res = input("Do you wish to continue(Y/N): ").strip().upper()
    if res in "YN":
        if res == "Y":
            continue
        else:
            break
    else:
        print("Invalid!!")

print(f"\n{'='*20}\n")
print(f"the total spent is {total}.")
print(f"{products_over_thousand} products cost more than $1000.")
print(f"{name_of_cheapest} is the cheapest product.")
