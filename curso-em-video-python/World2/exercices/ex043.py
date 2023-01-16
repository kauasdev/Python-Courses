height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

imc = weight / height ** 2
print("IMC: {:.2f}\n".format(imc))

if imc < 18.5:
    print("Underweight")
elif 18.5 <= imc <= 25:
    print("Ideal weight")
elif 25 < imc <= 30:
    print("Overweight")
elif 30 < imc <= 40:
    print("Obesity") 
elif imc > 40:
    print("Morbid obesity")