from coder import Coder
import string

morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
         "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
if __name__ == "__main__":
    translator = Coder(string.ascii_lowercase, string.ascii_uppercase)

    while (1):
        line = raw_input()
        coded = translator.encode(line)
        print coded
        print translator.decode(coded)
