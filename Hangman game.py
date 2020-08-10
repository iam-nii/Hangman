# This is a very simple Hangman game designed with python.
import random
import time #import time module


Difficulty_Level = input("Difficulty Level(Easy,Medium,Hard):")


# here we set the secret words
Secret_word = ["Princess","Pillar","Envelope","Barrier","Calender","Marble","Mineral"]

# This code makes sure that random words are chosen in the course of the game.
word = random.choice(Secret_word)

# Introductory code.
Length = len(word)
name = input("What is your name?")
print("Hello " + name, '!, time to play Hangman')

time.sleep(2) # wait for 2 seconds
print("Please wait while your game loads...")

time.sleep(5) # wait for 5 seconds
count = 0

# Displaying the length of the 'secret word'
display = '*' * Length

# Game begins!
def hangman(count, display, word):
    limit = 4  # Determines the number of tries
    guess = input('Your word is ' + display + ' |Go ahead and guess :)')
    # Creating the while loop
    # If the guess is in the secrete word display the position of that letter in the word.
    if guess in word:
        index = word.find(guess)
        word = word[:index]+ "*" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display)
    # If the guesses are  not in the secrete word, display the figures below
    else:
        count +=1
        if count == 1: # first wrong guess
            print("Wrong guess! "+ str(limit - count) + " guesses remaining")
            print( "__________\n"
                   "|         | \n"
                   "|         | \n"
                   "|         O \n"
                   "|           \n"
                   "|           \n"
                   "|           \n"
                   "|\ \n"
                   "|_\ \n")
        elif count == 2: # Second wrong guess
             print("Wrong guess! " + str(limit - count) + " guesses remaining")
             print("__________\n"
                   "|         |\n"
                   "|         |\n"
                   "|         O\n"
                   "|        /|\ \n"
                   "|           \n"
                   "|           \n"
                   "|\ \n"
                   "|_\ \n")
        elif count == 3: # Third wrong guess
             print("Wrong guess! " + str(limit - count) + " guesses remaining \n THIS IS YOUR FINAL GUESS!!")
             print("__________\n"
                   "|         | \n"
                   "|         | \n"
                   "|         O \n"
                   "|        /|\ \n"
                   "|         | \n"
                   "|           \n"
                   "|\ \n"
                   "|_\ \n")
        elif count == 4: # Forth wrong guess, GAME OVER!!
             print("Wrong guess! \n YOU ARE HANGED \n GAME OVER!!1")
             print("__________\n"
                   "|         | \n"
                   "|         | \n"
                   "|         O \n"
                   "|        /|\  \n"
                   "|         | \n"
                   "|        / \ \n"
                   "|\ \n"
                   "|_\ \n"
                   )

  # If all guesses were correct the player wins the game.
    if word == '*' * Length:
        print("Congrats! You have guessed it successfully...")
    elif count != limit:
        hangman(count, display, word)

hangman(count, display, word)


