from operator import itemgetter

# Tuples -> ()
# Lists -> []
# Dictionaries -> {}

dictionary = dict()
# or
dictionary = {}
print(dictionary)  # {}

person = {"name": "Bruno Pacheco", "age": 30}
#         index        coin       index  coin
# print(person[0]) -> KeyError
print(person["name"])  # Bruno Pacheco
print(person["age"])  # 30

# print(f'{person['name']} is {person['age']} years old') -> error
# print(f"{person["name"]} is {person['age']} years old") - error
# "" => [''] | '' => [""]

person["sex"] = "M"
print(person)  # {'name': 'Bruno Pacheco', 'age': 30, 'sex': 'M'}

del person["age"]
print(person)  # {'name': 'Bruno Pacheco', 'sex': 'M'}]

print(person.values())  # dict_values(['Bruno Pacheco', 'M'])
print(person.keys())  # dict_keys(['name', 'sex'])
print(person.items())  # dict_items([('name', 'Bruno Pacheco'), ('sex', 'M')])

for k, v in person.items():
    print(f"{k}(keys) -- {v}(values)")

people = [{"name": "Kauã Lima", "age": 16}, {
    "name": "Gaby", "age": 15}, {"name": "Lorena", "age": 15}]
#                        1                                2                               3
print(people)
print(people[1]["name"])  # Gaby


# SORTING DICTIONARIES

game = {
    "player_1": 8,
    "player_2": 3,
    "player_3": 20,
    "player_4": 9
}

dict_sorted = sorted(game.items(), key=itemgetter(1), reverse=True)
# itemgetter(0) -> key (Ex.: player_1) | itemgetter(1) -> coin (Ex.: 9)
# reverse = False -> ascending order | reverse = True -> descending order
print(dict_sorted)
