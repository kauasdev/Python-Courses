# Repeat structure with logical test
# while condition:
#   The loo will run as long the condition is true

num = 1
even_num = odd_num = 0

while num != 0:
    num = int(input("Enter the number: "))
    if num != 0:
        if num % 2 == 0:
            even_num += 1
        else:
            odd_num += 1
print(f"You entered {even_num} even numbers and {odd_num} odd numbers.")
