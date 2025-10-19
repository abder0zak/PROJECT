import random

# List of possible words
words = ["python", "computer", "programming", "hangman", "science"]

# Choose a random word
word = random.choice(words)

# Create a list of underscores for each letter in the word
guessed_word = ["_"] * len(word)

# Number of allowed tries
tries = 6

# Store guessed letters
guessed_letters = []

print("🎮 Welcome to the Word Guessing Game!")
print("The word has", len(word), "letters.")

while tries > 0:
    print("\nWord:", " ".join(guessed_word))
    print("Tries left:", tries)
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong guess!")
        tries -= 1

    # Check if the word is fully guessed
    if "_" not in guessed_word:
        print("\n🎉 You win! The word was:", word)
        break
else:
    print("\n💀 You lose! The word was:", word)

