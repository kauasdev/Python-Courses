def show_help(key):
    print("="*30)
    text = f"{key.title()} command manual"
    print(f"{text:^30}")
    print("="*30)
    help(key)


key_word = input("Function or Library(or END to stop): ").strip()
if key_word.upper() == "END":
    quit()
else:
    show_help(key_word)
