words = ("Python", "Artificial Intelligence", "Machine Learning",
         "TensorFlow", "Pytorch", "Pandas", "Numpy", "Math", "Random")

for word in words:
    print(f"In the word '{word}' we have the vowels ", end='')
    for letter in sorted(word):
        if letter.lower() in "aeiou":
            print(f"{letter.lower()}, ", end='')
    print("\n")
