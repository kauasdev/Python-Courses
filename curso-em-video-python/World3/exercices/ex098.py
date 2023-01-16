from time import sleep


def counter(start, end, step=1):
    if step == 0:
        step = -1

    print("="*20)
    if start < end:
        print(f"{start} => {end}")
        for n in range(start, end + 1, step):
            if n == end:
                print(n)
            else:
                print(f"{n}, ", end='')
            sleep(0.4)
    elif start > end:
        print(f"{start} ==> {end}")
        for n in range(start, end - 1, step):
            if n == end:
                print(n)
            else:
                print(f"{n}, ", end='')
            sleep(0.4)

    print("="*20)


counter(1, 10)
counter(10, 0, -2)

start_num = int(input("Start: "))
end_num = int(input("End: "))
step_num = int(input("Step: "))

counter(start_num, end_num, step_num)
