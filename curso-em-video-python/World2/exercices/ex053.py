phrase = input("\nWrite a phrase: ").strip()

phrase = ''.join(phrase.split(' '))
phrase_inverted = ''.join(phrase.split(' '))[::-1]

if phrase == phrase_inverted:
    print("The phrase is a palindrome\n")
else:
    print("The phrase isn't palindrome\n")