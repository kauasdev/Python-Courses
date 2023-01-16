name = input("Write your name: ").strip()

first_name = name.split()[0]

name_len_no_spaces = len(name) - name.count(' ')

print(f'\nUpper Case: {name.upper()}')
print(f'Lower Case: {name.lower()}')
print(f'Number of letters(no spaces): {name_len_no_spaces}')
print(f'Number of first name letters: {len(first_name)}')
