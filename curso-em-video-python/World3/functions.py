# FUNCTIONS
# => A function is a routine that can accept arguments and returns one or more values.

# print() | len() | int() | float() | input() -> These are functions that
# already exist in python

# def -> word used to declare functions

def show_line():
    print("-" * 30)


def show_message(msg):
    # msg is a parameter
    show_line()
    print(msg)
    show_line()


# show_line()
# show_message("This is a parameter")
# msg = "This is a parameter"

def sum_num(a=0, b=0):
    return a + b


s = sum_num(3, 5)
print(s)


def sum_many(*args):
    print(f"Type {type(args)}: {args}")
    for arg in args:
        print(arg)
    # => *args allows us to pass a variable number of non-keyword arguments to a Python function.


sum_many(0, 4, 5, 6, 4, 5, 6)
# Type <class 'tuple'>: (0, 4, 5, 6, 4, 5, 6)


def double(lst):
    for i, v in enumerate(lst):
        lst[i] *= 2


lst1 = [2, 4, 6, 8, 10]
double(lst1)
print(lst1)
