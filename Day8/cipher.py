alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def encrypt(text, shift):
#     cypher_text=""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         cypher_text += new_letter
#     print(f"The data is: {cypher_text}")


# def decrypt(text, shift):
#     plain_text=""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The decrypted data is: {plain_text}")

def ceaser(text, shift, direction):
    data = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        data += alphabet[new_position]
    print(f"The encoded text is {data}")
        
is_done = False

while not is_done:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt and 'exit' for exit: \n")
    if direction == "encode":
        text = input("Type your message: \n").lower()
        shift = int(input("Type the shift number: \n"))
        # encrypt(text=text, shift=shift)
        ceaser(text=text, shift=shift, direction=direction)
    elif direction == "decode":
        text = input("Type your message: \n").lower()
        shift = int(input("Type the shift number: \n"))
        # decrypt(text=text, shift=shift)
        ceaser(text=text, shift=shift, direction=direction)
    elif direction == "exit":
        is_done = True
    else:
        print("try again")


