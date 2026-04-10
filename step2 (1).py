import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing (so you can see the word)
print(f"Pssst, the solution is {chosen_word}.")

# Create blanks
display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"

# Take input
guess = input("Guess a letter: ").lower()

# Replace blanks with correct guesses
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

# Show result
print(display)