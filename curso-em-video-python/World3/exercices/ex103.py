def new_player(name="<unknown>", goals=0):
    print(f"The player {name.title()} scored {goals} goals")


name = input("Name: ")
goal = input("Goals: ")
if goal.isnumeric():
    goal = int(goal)
else:
    goal = 0

if name.strip() == "":
    new_player(goals=goal)
else:
    new_player(name, goal)
