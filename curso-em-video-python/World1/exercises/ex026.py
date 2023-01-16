phrase = input("Write any sentence: ").strip()

first_index_a = phrase.lower().find('a')
last_index_a = phrase.lower().rfind('a')

print(f"""\nPhrase: {phrase}

Number of letters 'A': {phrase.lower().count('a')}
First Index of 'A': {first_index_a + 1}
Last Index of 'A': {last_index_a + 1}""")