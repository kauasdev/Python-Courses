anything = input("Type anything: ")

type = type(anything)
is_num = anything.isnumeric()
is_str = anything.isalpha()
is_upe = anything.isupper()
is_low = anything.islower()

print(f'{anything}:\n Type: {type} \n Is Num: {is_num} \n Is String: {is_str} \n Is UpperCase: {is_upe} \n Is LowerCase: {is_low}')