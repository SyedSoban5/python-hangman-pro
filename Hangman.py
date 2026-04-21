import random

lives = 4
secret_word = "vibing"
display = ["_"] * len(secret_word)

print("--- Secret Word Guess Game ---")

print(" ".join(display))

while '_' in display and lives > 0:
    guess = input("\nGuess one letter: ").lower()

    if guess in secret_word:
        # Loop through to find all matches
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess
        
        print("Good job! Current progress: " + " ".join(display))
        
    else:
        lives -= 1
        print(f"Wrong! Lives left: {lives}")
        print("Current progress: " + " ".join(display))

if "_" not in display:
    print("\n🎉 You won! The word was:", secret_word)
else:
    print("\n💀 Game over! The word was:", secret_word)