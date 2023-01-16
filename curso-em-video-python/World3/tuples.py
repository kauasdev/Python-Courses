# tuple = ("item1", "item2", "item3", "item4")
# # index ->  0/-4     1/-3     2/-2      3/-1
# print(len(tuple)) # return 4

# for i in tuple:
#     # i = "item1" => i = "item2" => i = "item3" => i = "item4"
#     print(i)

# # TUPLE ARE IMMUTABLE

lunch = ("Cake", "Juice", "Pizza", "Pie")
print(len(lunch))
print(lunch[2])
print(lunch[-1])

# lunch[2] = "Potato"
# TypeError: 'tuple' object does not support item assignment

# WAYS TO ITERATE TUPLES
print('='*25)
for food in lunch:
    print(food)
print('='*25)
for count in range(0, len(lunch)):
    print(f"{count + 1}° -> {lunch[count]}")
print('='*25)
for i, food in enumerate(lunch):
    print(f"{i + 1}° -> {food}")


# METHODS
print(sorted(lunch)) # show the tuple in order


a = (1, 2, 3, 4, 3)
b = (6, 7, 8, 9, 3)

c = a + b

print('='*25)
print(c)
print(c.count(3))
print(c.index(2)) # returns the first occurrence
print(c.index(3, 5)) # returns the third occurrence

person = ("Kauã", 16, "M", 57.2)
del(person) # delete the tuple
print(person) # NameError: name 'person' is not defined