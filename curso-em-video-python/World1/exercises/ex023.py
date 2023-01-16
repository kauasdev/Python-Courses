num = int(input("Write a number between 0 and 9999: "))

if num < 0 or num > 9999:
    print('Invalid number!')
    quit()

u = num // 1 % 10
t = num // 10 % 10
h = num // 100 % 10
m = num // 1000 % 10

print(f"""\nNumber: {num}
Units: {u}
Tens: {t}
Hundred: {h}
Thousands: {m}""")