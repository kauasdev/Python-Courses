def line(txt_l=0):
    print("=" * txt_l)


def write(txt=""):
    txt_len = len(txt) + 4
    line(txt_len)
    print(f"{txt:^{txt_len}}")
    line(txt_len)


text = input("Write something: ")
write(text)
