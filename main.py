from replit import clear
import random
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 11
from hangman_art import logo, stages
print(logo)
display = []
for _ in range(word_length):
    display += "_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
      print(f"You've already chosen {guess}, see.")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You've guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            clear()
            end_of_game = True
            print(f"You lose, The word was '{chosen_word}' \n Try again.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("Congratulations, You win.")
    print(stages[lives])
