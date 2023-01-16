num1 = int(input("Enter the number: ")) 
num2 = int(input("Enter the number: ")) 
num3 = int(input("Enter the number: ")) 
num4 = int(input("Enter the number: ")) 

tuple = (num1, num2, num3, num4)

value_9 = tuple.count(9)
even_values = 0

for num in tuple:
    if num % 2 == 0:
        even_values += 1
    else:
        continue

print(f"\nThe value 9 appeared {value_9} times")
if 3 in tuple:
    print(f"The first 3 is at position {first_3}")
else:
    print("The number 3 was not entered")
print(f"{even_values} even numbers were en")