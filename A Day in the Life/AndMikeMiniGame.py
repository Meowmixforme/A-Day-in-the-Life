# Mike Pitchers 20/03/2019


print ("Welcome to Locate The O, a graph based mini-game!\n")
print ("You have 3 attempts of each question, failure to answer correctly\n"
       "within these 3 attempts will result in a fail and will move onto the next question\n")
print ("To get the question correct, your answer should \n"
       "be typed in the following format: 'Y#,X#'\n"
       "\n")

#varibles
guess = str("0")
answer = str("Y2,X3")
tries = 0
score = 0

while guess.upper() != answer and tries <3:
    # put question in quotes below
    guess = input("What is the location of 'O'? Remeber the format:'Y#,X#'\n"
                  "          Y\n"
                  "         4|\n"
                  "         3|\n"
                  "         2|    O\n"
                  "         1|\n"
                  " - - - - 0|- - - - -X\n"
                  "-4-3-2-1-1|1 2 3 4 5\n"
                  "        -2|\n"
                  "        -3|\n"
                  "        -4|\n"
                  "Answer:")
    if guess.upper() == answer:
          score = score + 1
          print ("\nYou are correct, well done!\n"
                 "Your score is", (score),"!\n"
                 "Let's move onto the next question.\n")
                   
    else:
      print ("\nThat answer is incorrect, please try again!\n")
      tries = tries + 1


guess = str("0")
answer = str("Y-2,X-2")
tries = 0

while guess.upper() != answer and tries <3:
    guess = input("What is the location of 'O'? Remeber the format:'Y#,X#'\n"
                  "          Y\n"
                  "         4|\n"
                  "         3|\n"
                  "         2|\n"
                  "         1|\n"
                  " - - - - 0|- - - - -X\n"
                  "-4-3-2-1-1|1 2 3 4 5\n"
                  "     O  -2|\n"
                  "        -3|\n"
                  "        -4|\n"
                  "Answer:")
    if guess.upper() == answer:
          score = score + 1  
          print ("\nYou are correct, well done!\n"
                 "Your score is", (score),"!\n"
                 "Let's move onto the next question.\n")
                  
    else:
      print ("\nThat answer is incorrect, please try again!\n")
      tries = tries + 1


guess = str("0")
answer = str("Y4,X-1")
tries = 0

while guess.upper() != answer and tries <3:
    guess = input("What is the location of 'O'? Remeber the format:'Y#,X#'\n"
                  "          Y\n"
                  "       O 4|\n"
                  "         3|\n"
                  "         2|\n"
                  "         1|\n"
                  " - - - - 0|- - - - -X\n"
                  "-4-3-2-1-1|1 2 3 4 5\n"
                  "        -2|\n"
                  "        -3|\n"
                  "        -4|\n"
                  "Answer:")
    if guess.upper() == answer:
          score = score + 1 
          print ("\nYou are correct, well done!\n"
                 "Your score is", (score),"!\n"
                 "Let's move onto the next question.\n")
                   
    else:
      print ("\nThat answer is incorrect, please try again!\n")
      tries = tries + 1

guess = str("0")
answer = str("Y0,X3")
tries = 0

while guess.upper() != answer and tries <3:
    guess = input("What is the location of 'O'? Remeber the format:'Y#,X#'\n"
                  "          Y\n"
                  "         4|\n"
                  "         3|\n"
                  "         2|\n"
                  "         1|\n"
                  " - - - - 0|- - O - -X\n"
                  "-4-3-2-1-1|1 2 3 4 5\n"
                  "        -2|\n"
                  "        -3|\n"
                  "        -4|\n"
                  "Answer:")
    if guess.upper() == answer:
          score = score + 1 
          print ("\nYou are correct, well done!\n"
                 "Your score is", (score),"!\n"
                 "Let's move onto the next question.\n")
                   
    else:
      print ("\nThat answer is incorrect, please try again!\n")
      tries = tries + 1




guess = str("0")
answer = str("Y-4,X5")
tries = 0

while guess.upper() != answer and tries <3:
    guess = input("What is the location of 'O'? Remeber the format:'Y#,X#'\n"
                  "          Y\n"
                  "         4|\n"
                  "         3|\n"
                  "         2|\n"
                  "         1|\n"
                  " - - - - 0|- - - - -X\n"
                  "-4-3-2-1-1|1 2 3 4 5\n"
                  "        -2|\n"
                  "        -3|\n"
                  "        -4|        O\n"
                  "Answer:")
    if guess.upper() == answer:
        score = score + 1 
        print ("\nYou are correct, well done!\n"
                 "Your score is", (score),"!\n"
                 "Let's move onto the next question.\n")
                  
    else:
      print ("\nThat answer is incorrect, please try again!\n")
      tries = tries + 1      

guess = str("0")
answer = str("Y-1,X-4")
tries = 0

while guess.upper() != answer and tries <3:
    guess = input("What is the location of 'O'? Remeber the format:'Y#,X#'\n"
                  "          Y\n"
                  "         4|\n"
                  "         3|\n"
                  "         2|\n"
                  "         1|\n"
                  " - - - - 0|- - - - -X\n"
                  " O-3-2-1-1|1 2 3 4 5\n"
                  "        -2|\n"
                  "        -3|\n"
                  "        -4|\n"
                  "Answer:")
    if guess.upper() == answer:
          score = score + 1 
          print ("\nYou are correct, well done!\n"
                 "Your score is", (score),"!\n"
                 "Let's move onto the next question.\n")
                   
    else:
      print ("\nThat answer is incorrect, please try again!\n")
      tries = tries + 1

guess = str("0")
answer = str("Y-1,X2")
tries = 0      

while guess.upper() != answer and tries <3:
    guess = input("What is the location of 'O'? Remeber the format:'Y#,X#'\n"
                  "          Y\n"
                  "          |\n"
                  "          |\n"
                  "          |\n"
                  "          |\n"
                  " - - - -  | - - - - -X\n"
                  "          |   O\n"
                  "          |\n"
                  "          |\n"
                  "          |\n"
                  "Answer:")
    if guess.upper() == answer:
          score = score + 1 
          print ("\nYou are correct, well done!\n"
                 "Your score is", (score),"!\n"
                 "Let's move onto the next question.\n")
                   
    else:
      print ("\nThat answer is incorrect, please try again!\n")
      tries = tries + 1

guess = str("0")
answer = str("Y-4,X-1")
tries = 0
      
while guess.upper() != answer and tries <3:
    guess = input("What is the location of 'O'? Remeber the format:'Y#,X#'\n"
                  "          Y\n"
                  "          |\n"
                  "          |\n"
                  "          |\n"
                  "          |\n"
                  " - - - -  | - - - - -X\n"
                  "          |\n"
                  "          |\n"
                  "       O  |\n"
                  "          |\n"
                  "Answer:")
    if guess.upper() == answer:
          score = score + 1 
          print ("\nYou are correct, well done!\n"
                 "Your score is", (score),"!\n"
                 "Let's move onto the next question.\n")
                    
    else:
      print ("\nThat answer is incorrect, please try again!\n")
      tries = tries + 1


print ("Congratulations, you have finished Locate The O!!\n")

if score == 8:
          print("You scored the maximum of 8 points!\n Congratulations!!!")


else:
          print("You scored a total of: ",(score), " Well done! But not quite the best yet!")


    

    
