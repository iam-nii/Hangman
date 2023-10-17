# Step 1
import random
import hangman_art
import words

stages = hangman_art.stages
word_list = words.word_list
logo = hangman_art.logo

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable
# called chosen_word.
chosen_word = random.choice(word_list)
print(logo)

# TODO-2 - Create blanks as long as the chosen word and store them in an array
word_length = len(chosen_word)
word_array = []

for num in range(0, word_length):
    word_array.append("_")

game_over = False
lives = 6

while not game_over or lives > 0:
    # TODO-3 - Ask the user to guess a letter and assign their answer to a variable
    # called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()

    # TODO-4 - Check if the letter the user guessed (guess) is one of the letters in
    # the chosen_word.
    #index = 0
    for position in range(word_length):
        if chosen_word[position] == guess:
            if word_array[position] == guess:
                print(f"You've already guessed '{guess}' :)")
            else:
                word_array[position] = guess

    #Tracking the players life and reducing it if the guess is not in the chosen
    #word
    if guess not in chosen_word:
        print(f"{guess} is not in the word, you lose a life :(")
        print(stages[lives])
        lives -= 1
    else:
        print(word_array)

    #Checking to see if all the blanks have been filled or the player is still alive
    if "_" not in word_array:
        game_over = True
        print("You win!!")
    elif lives < 0:
        game_over = True
        print("Game Over! you lose!")
