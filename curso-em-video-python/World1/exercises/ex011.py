height = float(input("Enter the height of the wall: "))
width = float(input("Enter the width of the wall: "))

area_wall = height * width

amount_of_ink = int(area_wall // 2)

print(" Area wall: {:.2f} meters \n Amount of ink: {} liters". format(area_wall, amount_of_ink))