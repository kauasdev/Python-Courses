house_value = float(input("What's the coin of the house: "))
salary = float(input("What's your salary: "))
years = int(input("How many years will you pay: "))

months = years * 12
installments = house_value / months

if installments > (salary * 0.3):
    print("Loan rejected!")
else:
    print("Approved Loan")