def coin(value):
    value = str(value)
    find_dot = value.find(".")

    if find_dot != -1:
        removed_dot = value.replace(".", ",")
        return f"RS{removed_dot}"
    else:
        return f"R${value},00"


def half(value, format_price=False):
    result = value / 2
    if format_price:
        return coin(result)
    else:
        return result


def double(value, format_price=False):
    result = value * 2

    if format_price:
        return coin(result)
    else:
        return result


def increase(value, incre, format_price=False):
    inc = value * (incre / 100)
    result = value + inc

    if format_price:
        return coin(result)
    else:
        return result


def reduction(value, reduc, format_price=False):
    red = value * (reduc / 100)
    result = value - red

    if format_price:
        return coin(result)
    else:
        return result


def summary(value, incre=0, reduc=0, format_price=False):
    print("-"*30)
    print(f"{'Value Summary':^30}")
    print("-"*30)
    print(f"Half: {half(value, format_price)}")
    print(f"Double: {double(value, format_price)}")
    print(f"Increasing {incre}%: {increase(value, incre, format_price)}")
    print(f"Reducing {reduc}%: {reduction(value, reduc, format_price)}")
