less_weight = float(input("Enter the weight: "))
greater_weight = 0

for people in range(1, 5):
    weight = float(input("Enter the weight: "))

    if weight > greater_weight:
        greater_weight = weight
    elif weight < less_weight:
        less_weight = weight
    else:
        pass

print(f"\n{'='*24}")
print(f"Greater weight: {greater_weight}")
print(f"Less weight: {less_weight}")
