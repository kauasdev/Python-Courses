def test(b):

    global d  # The global command allows to use a global variable in the local scope, without creating a new variable
    a = 8  # This 'a' is a local variable
    # Create a new variable 'a' different from the global variable 'a'
    b += 4
    c = 2
    d = 99

    print(f"'A' inside is equal to {a}")
    print(f"'B' inside is equal to {b}")
    print(f"'C' inside is equal to {c}")


a = 5  # This 'a' is a global variable
d = 4  # This 'd' is a global variable
print(f"'D' outside is equal to {d}")
test(a)
print(f"'A' outside is equal to {a}")
print(f"'D' outside is equal to {d} now")
