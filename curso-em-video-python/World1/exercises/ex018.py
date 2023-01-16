from math import radians, cos, sin, tan

angle = int(input("Enter the angle coin: "))

cosine = cos(radians(angle))
sine = sin(radians(angle))
tangent = tan(radians(angle))

print('='*15)
print('Angle: {}° \n\nSine: {:.2f}\nCosine: {:.2f}\nTangent: {:.2f}'.format(
    angle, sine, cosine, tangent))
print('='*15)
