from coder import Coder, MorseCoder
import string

if __name__ == "__main__":
    # By default, the translator will encode files by switching them to uppercase
    translator = Coder(string.ascii_lowercase, string.ascii_uppercase)

    while (1):
        line = raw_input()
        coded = translator.encode(line)
        print coded
        print translator.decode(coded)
