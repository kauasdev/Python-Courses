from math import factorial as fac


def factorial(n, show=False):
    """
    :param n: The number to be calculated
    :param show: (Optional) Whether the show the calculation
    :return: Factorial of n
    """
    print("="*30)
    if show:
        total_fac = n
        print(f"{n} x ", end='')
        for i in range(n-1, 1, -1):
            total_fac *= i
            print(f"{i} x ", end='')
        print(f"1 = {total_fac}")
    else:
        print(f"The factorial of {n} is {fac(n)}")
    print("="*30)


num = int(input("Enter a number: "))
show_cal = input("Show calculation(Y/N): ").strip().upper()
if show_cal in "YN":
    if show_cal == "Y":
        show_cal = True
    else:
        show_cal = False

factorial(num, show_cal)
help(factorial)
