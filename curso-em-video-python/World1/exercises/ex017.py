from math import hypot

print('='*40)
opposite_side = float(input("Enter the coin of the opposite side: "))
adjacent_side = float(input("Enter the coin of the adjacent side: "))

hypotenuse = ((opposite_side ** 2) + (adjacent_side ** 2)) ** (1/2)
hypo = hypot(opposite_side, adjacent_side)

print('{:.2f}'.format(hypo))
print('\nThe coin of the hypotenuse is {:.2f}'.format(hypotenuse))
print('='*40)
