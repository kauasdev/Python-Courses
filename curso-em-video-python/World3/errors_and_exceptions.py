a = 3
# resul = a + b  # b is not defined
# Traceback (most recent call last):
#     resul = a + b
# NameError: name 'b' is not defined


c = "6"
# resul = a + c  # c is a string
# Traceback (most recent call last):
#     resul = a + c
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


# result = a / 0
# Traceback (most recent call last):
#     result = a / 0
# ZeroDivisionError: division by zero

# try: (Mandatory)
#     code
# except: (Mandatory)
#     if there is error
# else: (Optional)
#     if there is no error
# finally: (Optional)
#     will be executed no matter if the
#     try block raises an error or not.


try:
    num1 = int(input("Enter the number: "))
    num2 = int(input("Enter the number: "))
    div = num1 / num2
# except Exception as error:
#     print(f"Error!! Error: {error.__class__}")
except (ValueError, TypeError):  # (error, error)
    print("Just type numbers!")
except ZeroDivisionError:
    print("It is not possible to do a division by zero")
except Exception as error:
    print(f"Error: {error.__class__}")
else:
    print(div)
finally:
    print("Finished!")
