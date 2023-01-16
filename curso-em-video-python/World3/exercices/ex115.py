import os
from ex115_packages import register_person, list_people, clear_list


path = os.path.dirname(__file__)
file = path + "/people_list.txt"
print(file)

if not os.path.exists(file):
    open(file, "w")

while True:
    action = input("""Choose an action:
    
    1 - Register a new person
    2 - List people
    3 - Clear list
    4 - Stop
    
    => """)

    if action not in "1234":
        print("Invalid action!")

    else:
        if action == "1":
            register_person(file)
        elif action == "2":
            list_people(file)
        elif action == "3":
            clear_list(file)
        else:
            break
