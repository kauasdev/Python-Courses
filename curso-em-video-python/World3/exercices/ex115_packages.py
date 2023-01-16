import json
import os
from time import sleep


def register_person(file):
    person = dict()
    while True:
        try:
            name = input("Name: ")
            age = int(input("Age: "))
        except (ValueError, TypeError):
            print("Please enter valid information!")
        else:
            person["name"] = name
            person["age"] = age
            break

    person_txt = json.dumps(person)

    with open(file, "r") as data_lines:
        line = ''
        if not data_lines.readlines():
            line = f"{person_txt}"
        else:
            line = f"\n{person_txt}"
        with open(file, "a") as data:
            data.write(line)
            print(f"{person['name']} registered successfully!")


def load_people(file):
    people = list()
    person = dict()
    max_name_len = max_age_len = 0
    with open(file, "r") as data:
        for line in data.readlines():
            p = json.loads(line)
            if p:
                name, age = p.items()
                if len(name[1]) > max_name_len:
                    max_name_len = len(name[1])
                if len(str(age[1])) > max_age_len:
                    max_age_len = len(str(age[1]))

                person["name"] = name[1]
                person["age"] = age[1]
                people.append(person.copy())
    return [people, max_name_len, max_age_len]


def list_people(path):
    people, max_name_len, max_age_len = load_people(path)
    table_len = max_name_len + max_age_len + 6

    if not len(people):
        print("No records!")
        quit()

    if table_len > 14:
        print(f"\n| {'name':^{max_name_len}} | {'age':^{max_age_len}} |")
        table_len += 2
        print("-" * table_len)

        for person in people:
            sleep(0.3)
            print(f"| {person['name']:^{max_name_len}} | {person['age']:^{max_age_len + 1}} |")
    else:
        print("\n| name | age |")
        print("-" * 14)

        for person in people:
            name = f"| {person['name']}"
            age = f"{person['age']} |"
            sleep(0.3)
            print(f"{name:^{max_name_len}} | {age:^6}")
    print("")


def clear_list(path):
    if os.path.exists(path):
        with open(path, "w") as file:
            file.write("")
            print("Deleted records!")
    else:
        print("List not found!")
