import random

# List of words
words = ["apple", "tiger", "chair", "pizza", "robot"]

# Random word selection
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("🎮 Welcome to Hangman Game!")

while wrong_guesses < max_wrong_guesses:
    display_word = ""

    # Show guessed letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Win condition
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        wrong_guesses += 1
        print("❌ Wrong guess!")
        print("Remaining chances:", max_wrong_guesses - wrong_guesses)

# Lose condition
if wrong_guesses == max_wrong_guesses:
    print("\n💀 Game Over!")
    print("The word was:", word)