soccer_players = list()
player = dict()
cod = 1

while True:
    goals = list()
    player["cod"] = cod
    player["name"] = input("Name: ")
    games_played = int(input("How many games were played: "))
    player["games_played"] = games_played

    for gp in range(1, games_played + 1):
        goals.append(
            int(input(f"How many goals were scored in {gp}° match: ")))

    del player["games_played"]
    player["goals"] = goals
    player["total"] = sum(player["goals"])

    soccer_players.append(player.copy())
    cod += 1

    res = input("Do you wish to continue[Y/N]: ").strip().upper()
    if res in "YN":
        if res == "N":
            break
    else:
        break

print(f"\n{'cod':^5}{'name':^10}{'goals':^20}{'total':^6}")
print("-"*42)

for sp in soccer_players:
    cod, name, goals, total = sp.values()
    print(f"{cod:^5}{name:^10}{str(goals):^20}{total:^6}")

while True:
    cod_player = int(input("\nShow the data of which player(999 to stop): "))
    if cod_player == 999:
        break
    for p in soccer_players:
        if p["cod"] == cod_player:
            print(f"\n{p['name']} player numbers:\n")
            for i, g in enumerate(p["goals"]):
                print(f"    In game {i+1} the player scored {g} goals.")
