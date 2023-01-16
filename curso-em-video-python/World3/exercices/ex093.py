soccer_player = dict()
goals = list()
soccer_player["name"] = input("Name: ")
games_played = int(input("How many games were played: "))

for gp in range(1, games_played + 1):
    goals.append(int(input(f"How many goals were scored in {gp}° match: ")))

soccer_player["goals"] = goals

print("="*40)
print(
    f"\nThe soccer player {soccer_player['name']} played {games_played} matches.\n")
for i, g in enumerate(soccer_player["goals"]):
    print(f"=> In the {i + 1}st match, scored {g} goals.")
print(f"\nIn total, there were {sum(soccer_player['goals'])} goals.")
