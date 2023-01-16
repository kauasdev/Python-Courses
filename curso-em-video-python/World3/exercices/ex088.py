from random import randint
from time import sleep

num_of_games = int(input("How many games do you want to draw: "))
games = list()

for g in range(0, num_of_games):
    game = []

    for n in range(0, 6):
        game.append(randint(1, 60))

    games.append(game[:])

print(f"\n{'='*40}\n")
for i, gs in enumerate(games):
    print(f"{i+1}st game -> {gs}")
    sleep(0.8)
print(f"\n{'='*40}\n")
