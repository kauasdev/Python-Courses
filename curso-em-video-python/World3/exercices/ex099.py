def larger(*args):
    if len(args):
        larger_value = max(args)
        print(f"Total: {len(args)} values => ", end='')
        print(list(args))
        print(f"The biggest value is {larger_value}")
    else:
        print("No values!")


larger(4, 5, 2, 777, 292828, 444, 1, 324324324, 9 ** 19)
larger()
