people = []

pedro = ["Pedro", 35]
paulo = ["Paulo", 45]
gaby = ["Gaby", 16]

people.append(pedro)
people.append(paulo)
people.append(gaby)

print(people)
# [['Pedro', 35], ['Paulo', 45], ['Gaby', 16]]
#     0      1        0      1      0     1
#        0               1             2

print(people[0][0])  # Pedro
print(people[1])