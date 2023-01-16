number = int(input("Enter an integer: "))
convert_to = int(input("""Type it:
1 for binary
2 for octal
3 to hex

----> """))

if convert_to == 1:
    print(f"{number} converted to binary equals {bin(number)[2:]}")
elif convert_to == 2:
    print(f"{number} converted to octal equals {oct(number)[2:]}")
elif convert_to == 3:
    print(f"{number} converted to hex equals {hex(number)[2:]}")
else:
    print("Invalid action!")