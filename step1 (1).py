import random

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word
chosen_word = random.choice(word_list)

# Ask user for input
guess = input("Guess a letter: ").lower()

# Check each letter
for letter in chosen_word:
    if letter == guess:
        print("Correct!")
    else:
        print("Incorrect!")

# Show the word (for testing)
print(f"The word is: {chosen_word}")