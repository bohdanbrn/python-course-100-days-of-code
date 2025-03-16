import art

print(art.logo)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def generate_alphabet_data(direction, shift_amount):
    alphabet_data = {}
    alphabet_length = len(alphabet)

    for letter in alphabet:
        letter_index = alphabet.index(letter)
        new_letter_index = 0

        if direction == "encode":
            new_letter_index = letter_index + shift_amount
        else:
            new_letter_index = letter_index - shift_amount

        new_letter_index = new_letter_index % alphabet_length

        alphabet_data[letter] = alphabet[new_letter_index]

    return alphabet_data


def caesar(direction, text, shift_amount):
    caesar_data = generate_alphabet_data(direction, shift_amount)
    result = ""

    for letter in text:
        new_letter = ""
        if letter in caesar_data:
            new_letter = caesar_data[letter]
        else:
            new_letter = letter

        result += new_letter

    print(f"Here is the {direction}d result: {result}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
