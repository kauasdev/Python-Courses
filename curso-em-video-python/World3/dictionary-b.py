people = list()
person = dict()

for i in range(0, 3):
    person["name"] = input("What's your name? ")
    person["age"] = int(input("How old are you? "))

    people.append(person.copy())

print(people)