import random
from hangman_words import word_list
from hangman_art import stages, logo

PLACEHOLDER_SYMBOL = "_"
NUMBER_OF_LIVES = 6


def display_current_state(stages, NUMBER_OF_LIVES):
    print(stages[NUMBER_OF_LIVES])


print(logo)
display_current_state(stages, NUMBER_OF_LIVES)

chosen_word = random.choice(word_list)
placeholder = PLACEHOLDER_SYMBOL * len(chosen_word)
display = list(placeholder)

while PLACEHOLDER_SYMBOL in display:
    guess = input("Guess a letter: ").lower()

    if guess not in chosen_word:
        NUMBER_OF_LIVES -= 1

        print(f"You guessed {guess}, that's not in the word. You lose a life. {NUMBER_OF_LIVES} lives left.")
        display_current_state(stages, NUMBER_OF_LIVES)

        if NUMBER_OF_LIVES == 0:
            print(f"It was '{chosen_word}'! You lose.")
            exit()
    elif guess in display:
        print(f"You've already guessed {guess}")
        continue

    for letterIndex in range(len(chosen_word)):
        if chosen_word[letterIndex] == guess:
            display[letterIndex] = guess

    print("".join(display))


print("You win.")
