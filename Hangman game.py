# This is a very simple Hangman game designed with python.
import random
import time


Difficulty_Level = input("Difficulty Level(Easy,Medium,Hard):")



Secret_word = ["Princess","Pillar","Envelope","Barrier","Calender","Marble","Mineral"]
word = random.choice(Secret_word)
Length = len(word)
name = input("What is your name?")
print("Hello " + name, '!, time to play Hangman')
time.sleep(2)
print("Please wait while your game loads...")
time.sleep(5)
count = 0
display = '*' * Length


def hangman(count, display, word):
    limit = 4
    guess = input('Your word is ' + display + ' |Go ahead and guess :)')
    if guess in word:
        index = word.find(guess)
        word = word[:index]+ "*" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display)
    else:
        count +=1
        if count == 1:
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
        elif count == 2:
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
        elif count == 3:
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
        elif count == 4:
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


    if word == '*' * Length:
        print("Congrats! You have guessed it successfully...")
    elif count != limit:
        hangman(count, display, word)

hangman(count, display, word)

