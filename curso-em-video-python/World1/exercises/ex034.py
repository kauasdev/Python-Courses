salary = float(input("Whats's the employee's salary: "))

if salary > 1250:
    new_salary = salary + (salary * 0.10)
    print(f"New salary: {new_salary}")
else:
    new_salary = salary + (salary * 0.15)
    print(f"New salary: {new_salary}")