import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
end_of_game = False

display = ["_"] * word_length
guessed_letters = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'")
        continue
    guessed_letters.append(guess)

    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        print(f"You guessed '{guess}', that's not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose! The word was '{chosen_word}'")

    print(" ".join(display))
    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win!")