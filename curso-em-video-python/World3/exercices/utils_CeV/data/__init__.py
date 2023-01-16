def read_money(msg):
    while True:
        value = input(msg).replace(",", ".").strip()

        if value.isalpha() or value == "":
            print(f"'{value}' is an invalid price!")
        else:
            return float(value)


def read_int(value):
    return 1


def read_float(value):
    return 0
