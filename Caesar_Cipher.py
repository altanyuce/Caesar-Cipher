from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % 26

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    if letter == " ":
        cipher_text += letter
    else:
        position = alphabet.index(letter)
        new_position = (position + shift_amount) % 26
        cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        if letter == " ":
            plain_text += letter
        else:
            position2 = alphabet.index(letter)
            new_position2 = (position2 - shift_amount) % 26
            plain_text += alphabet[new_position2]
    print(f"The decoded text is {plain_text}")

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
