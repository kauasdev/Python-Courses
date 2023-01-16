from random import randint
from time import sleep
from operator import itemgetter

game = {
    "player_1": randint(1, 6),
    "player_2": randint(1, 6),
    "player_3": randint(1, 6),
    "player_4": randint(1, 6)
}

ranking = dict()

for k, v in game.items():
    player = " ".join(k.split("_")).title()
    print(f"{player} played {v}")
    sleep(0.5)

ranking = sorted(game.items(), key=itemgetter(1), reverse=True)

print("\nRanking")
for i, p in enumerate(ranking):
    player = " ".join(p[0].split("_")).title()
    print(f"{i+1}° {player}: {p[1]}")
