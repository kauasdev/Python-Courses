list_test = ["item1", "item2", "item3"]
#           0         1        2
print(list_test)
# LIST ARE NOT IMMUTABLE

list_test.append("item4")  # -> Add an item to the end of the list
# list_test.append(int(input("Enter the number between 0 and 10: ")))
print(list_test)

list_test.insert(1, "item5")  # -> Adds an item at the desired position
print(list_test)

del list_test[3]  # -> Delete an item from the list
print(list_test)

list_test.pop()  # -> Delete the last item in the list
print(list_test)

list_test.pop(2)  # -> Delete an item from the list by its index
print(list_test)

list_test.remove("item1")  # -> Delete an item from the list by its coin

# Creating lists from ranges
list_from_range = list(range(1, 11))
print(list_from_range)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sort_list = [9, 3, 5, 7, 1000, 2, 4, 8, 20, 3]
print(sorted(sort_list))  # -> Function returns a sorted list
# [2, 3, 3, 4, 5, 7, 8, 9, 20, 1000]
print(sorted(sort_list, reverse=True))
# [1000, 20, 9, 8, 7, 5, 4, 3, 3, 2]

print(len(sort_list))  # -> Returns the length of the list

# LINK BETWEEN LISTS

a = [1, 2, 3, 4, 5]
b = a  # link

print(f"List A: {a}")  # [1, 2, 3, 4, 5]
print(f"List B: {b}\n")  # [1, 2, 3, 4, 5]

b[3] = 8  # -> b == a

print(f"List A: {a}")  # [1, 2, 3, 8, 5]
print(f"List B: {b}\n")  # [1, 2, 3, 8, 5]

# Copy Lists

c = a[:] # no link/connection with a
# a == [1, 2, 3, 8, 5]
print(c) # c == [1, 2, 3, 8, 5]
c[1] = 7
print(c) # c == [1, 7, 3, 8, 5]
print(a) # a == [1, 2, 3, 8, 5]
