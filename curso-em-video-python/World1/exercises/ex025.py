name = input("Write your name: ")

name_contains_silva = name.lower().find('silva')

if name_contains_silva != -1:
    print("Your name contains 'SILVA'")
else:
    print("Your name does not contain SILVA")