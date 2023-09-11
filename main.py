def caesar(text, shift, direction):
    global cipher_text

    cipher_text = ""
    if direction == "decode":
        shift = shift * -1

    for i in text:
        if i in alphabet:
            shift_amount = (int(alphabet.index(i)) + shift) % 26
            cipher_text += alphabet[shift_amount]
        else:
            cipher_text += i

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from ascii import logo
print(logo)

should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(text, shift, direction)
    print(f"{direction}d word is '{cipher_text}'.")

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True