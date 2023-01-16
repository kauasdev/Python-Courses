from random import randint
from time import sleep

user_choice = int(input("""Choose one:

1 - Rock
2 - Paper
3 - Scissors

-----> """))

pc_actions = ['rock', 'paper', 'scissors']
pc_choice = pc_actions[randint(0,2)]

print("The computer is choosing...")
sleep(2)

print(f"\nThe computer chose {pc_choice}")

if user_choice == 1 and pc_choice == 'rock':
    print("None won")
elif user_choice == 1 and pc_choice == 'paper':
    print("You lose")
elif user_choice == 1 and pc_choice == 'scissors':
    print("You win")

elif user_choice == 2 and pc_choice == 'paper':
    print("None won")
elif user_choice == 2 and pc_choice == 'scissors':
    print("You lose")
elif user_choice == 2 and pc_choice == 'rock':
    print("You win")

elif user_choice == 3 and pc_choice == 'scissors':
    print("None won")
elif user_choice == 3 and pc_choice == 'rock':
    print("You lose")
elif user_choice == 3 and pc_choice == 'paper':
    print("You win")