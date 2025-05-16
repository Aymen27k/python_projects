import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True


def caesar(start_text, shift_amount, cipher_direction):
    final_text = ""
    effective_shift = shift_amount % 26
    if cipher_direction == "decode":
        effective_shift *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + effective_shift
            final_text += alphabet[new_position]
        else:
            final_text += char
    print(f"The {cipher_direction}d code is {final_text}")


print(art.logo)
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("TyEnter the text you want to encrypt or decrypt:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    user_decision = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if user_decision == "no":
        should_continue = False
        print("GoodBye!")
