import ascii_art
import lists


def caesar(text, shift, direction):
    shift = int(shift)
    encript = False
    encode_word = []

    while not encript:
        while int(shift) >= 25:
            shift = input("write a number you shift:\n")
        shift = int(shift)
        for n in text:
            if n not in lists.alphabet:
                text = input("write your text:\n").lower()
            elif n in text:
                index_alphabet = lists.alphabet.index(n)
                if direction == "ENCODE":
                    letter_index = index_alphabet + shift
                elif direction == "DECODE":
                    letter_index = index_alphabet - shift
                letter_encode = lists.alphabet[letter_index]
                encode_word.append(letter_encode)

        if len(encode_word) == len(text):
            encript = True

    encode_word = ''.join(encode_word)
    print(encode_word)


def restart(again):
    if again == "YES":
        direction = input("Write what you want to make 'encode' or 'decode':\n").upper()
        text = input("write your text:\n").lower()
        shift = input("write a number you shift:\n")
        caesar(text, shift, direction)
    elif again == "NO":
        print("ByeBye")


print(ascii_art.logo[0])
direction = input("Write what you want to make 'encode' or 'decode':\n").upper()
text = input("write your text:\n").lower()
shift = input("write a number you shift:\n")

caesar(text, shift, direction)

again = input("You want to restart the program?, Type YES or NO").upper()

restart(again)
