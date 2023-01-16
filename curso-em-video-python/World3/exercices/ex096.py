def area(a=0.0, b=0.0):
    return a * b


length = float(input("Insert length: "))
width = float(input("Insert width: "))

land_area = area(length, width)
print(f"\nThe area is {land_area:.2f}m²")
