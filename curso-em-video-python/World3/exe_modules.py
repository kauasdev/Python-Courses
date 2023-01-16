def factorial(num):
    fac = num
    for i in range(num - 1, 0, -1):
        fac *= i

    return fac


def double(num):
    return num * 2


def triple(num):
    return num * 3
