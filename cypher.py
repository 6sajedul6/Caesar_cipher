alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(t,s):
    encrypted_text=""
    for i in t:
       position = alphabet.index(i)
       new_position= position+s
       new_letter=alphabet[new_position]
       encrypted_text+= new_letter
    print(f"The encoded text is {encrypted_text}.")


def decrypt(t,s):
    decrypted_text=""
    for i in t:
        position =alphabet.index(i)
        new_shift=shift
        new_positon=position-s
        new_letter=alphabet[new_positon]
        decrypted_text+=new_letter
    print(f"The decoded text is '{decrypted_text}'.")

if direction=="encode":
    encrypt(text,shift)
elif direction=="decode":
    decrypt(text,shift)
else:
    print("ERROR!!!! Please Type 'encode' to encrypt, type 'decode' to decrypt")