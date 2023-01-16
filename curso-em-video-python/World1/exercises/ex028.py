from random import randint
from time import sleep

pc_num = randint(0, 5)
while True:
    user_num = int(input("Guess a number between 0 and 5\n--> "))
    print("Processing...")
    sleep(1.5)
    if user_num == pc_num:
        print("Congratulations!")
        break
    else:
        print("Try again")
        pc_num = randint(0, 5)
