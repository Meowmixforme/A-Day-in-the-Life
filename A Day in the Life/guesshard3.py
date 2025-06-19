#17/02/2019 Hard Guessing number by James Fothergill

import random

randNum = random.randint(1, 250)
guesses = 0

for i in range(1, 4):
    guesses = guesses + 1
    print("Guess a number between 1 and 250 \n")
    guess = input()

    if guess.isdigit():
        if int(guess) > randNum:
            print("your guess is too high \n")

        elif int(guess) < randNum:
            print("your guess is too low \n")

        elif int(guess) == randNum:
            print("Congratulations!! \n")
            print("you needed " + str(guesses) + " guesses")
             
    else:
        print("Invalid Input! Try a number. \n")

print ("The Magic number was",(randNum))        

# Taken from https://stackoverflow.com/questions/50672297/python-3-number-guessing-game
