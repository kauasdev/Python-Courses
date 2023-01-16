soccer_teams = ("Palmeiras", "Internacional", "Flamengo", "Corinthians", "Fluminense", "Athletico-PR", "Atlético-MG", "América-MG", "Fortaleza",
                "São Paulo", "Botafogo", "Santos", "Bragantino", "Goiás", "Coritiba", "Ceará", "Cuiabá", "Atletico Goianiense", "Avaí", "Chapecoense")
break_row = f"\n{'='*20}\n"

print(break_row)
print(f"The first 5 teams are {soccer_teams[0:5]}")
print(break_row)
print(f"The last 4 teams are {soccer_teams[16:20]}")
print(break_row)
chape_pos = soccer_teams.index("Chapecoense")
print(f"Chapecoense's team is in {chape_pos}th position")
print(break_row)
