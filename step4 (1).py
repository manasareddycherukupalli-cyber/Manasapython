import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(f"Pssst, the solution is {chosen_word}.")

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
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")

        if lives == 0:
            end_of_game = True
            print(f"You lose! The word was '{chosen_word}'")

    print(" ".join(display))
    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win!")