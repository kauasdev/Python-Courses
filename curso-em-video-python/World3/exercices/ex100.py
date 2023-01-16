from random import randint

num_list = list()


def draw(lst=None, n=1):
    if lst is None:
        lst = []
    for i in range(0, n+1):
        lst.append(randint(1, 10))


def sum_even(lst):
    sum_num = 0
    for n in lst:
        if n % 2 == 0:
            sum_num += n
    return sum_num


draw(num_list, 5)
print(f"The values drawn were {num_list}")
print(f"The sum of the even values is {sum_even(num_list)}")
