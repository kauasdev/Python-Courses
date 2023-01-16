# DOCSTRING

# A Python docstring is a string used to document a Python module, class, function or method, so programmers can
# understand what it does without having to read the details of the implementation.

def counter(st, en, sp=1):
    """
    :param st: start
    :param en: end
    :param sp: step
    :return: none
    """
    # """ documentation """ => define a docstring
    for n in range(st, en, sp):
        print(f"{n}, ", end="")
    print()


counter(1, 10)
help(counter)
