expression_math = input("Write a mathematical expression with parentheses: ")
parentheses = inverted_parentheses = 0

for l in expression_math:
    if l == "(":
        parentheses += 1
    elif l == ")":
        inverted_parentheses += 1
    else:
        continue

if parentheses == inverted_parentheses:
    print(f"\nThe expression {expression_math} is valid")
else:
    print(f"\nThe expression {expression_math} isn't valid")
