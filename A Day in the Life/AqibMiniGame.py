# Aqib Ali 


print ("Welcome to the grocery list Mini-game\n")
print ("You have 3 attempts of each question \n"
       "If all your 3 attempts result in a fail, it will move onto the next question\n")
print (""
       "")

#variables
guess = 0
answer = str("£2.94")
tries = 0
score = 0

while guess != answer and tries <3:
    # put question in quotes below
    guess = input("Calculate the answer of the items on the reciept\n"
                  "  - - - - - - - -   \n"
                  "| Reciept          |\n"
                  "|                  |\n"
                  "| Potatoes £1.35   |\n"
                  "| Jam      £1.00   |\n"
                  "| Bread       59p  |\n"
                  "|                  |\n"
                  "|                  |\n"
                  "|                  |\n"
                  "|                  |\n"
                  "  - - - - - - - -   \n"
                  "Answer:")
    if guess == answer:
          score = score + 1
          print ("\n Well done!\n"
                 "Your score is", (score),"!\n"
                 "Let's move onto the next question.\n")
                   
    else:
      print ("Incorrect answer, please try again!\n")
      tries = tries + 1



guess = 0
answer = str("£2.06")
tries = 0


while guess != answer and tries <3:
    # put question in quotes below
    guess = input("Calculate the change you would get back from £5\n"
                  "  - - - - - - - -   \n"
                  "| Reciept          |\n"
                  "|                  |\n"
                  "| Potatoes £1.35   |\n"
                  "| Jam      £1.00   |\n"
                  "| Bread       59p  |\n"
                  "|                  |\n"
                  "|                  |\n"
                  "|                  |\n"
                  "|                  |\n"
                  "  - - - - - - - -   \n"
                  "Answer:")
    if guess == answer:
          score = score + 1
          print ("\n Well done!\n"
                 "Your score is", (score),"!\n"
                 "Let's move onto the next question.\n")
                   
    else:
      print ("Incorrect answer, please try again!\n")
      tries = tries + 1

guess = 0
answer = str("£12.72")
tries = 0


while guess != answer and tries <3:
    # put question in quotes below
    guess = input("Calculate the change you would get back from £20\n"
                  "  - - - - - - - -   \n"
                  "| Reciept          |\n"
                  "|                  |\n"
                  "| Lucozades £2.50  |\n"
                  "| Fruit mix £1.29  |\n"
                  "| Meat      £3.49  |\n"
                  "|                  |\n"
                  "|                  |\n"
                  "|                  |\n"
                  "|                  |\n"
                  "  - - - - - - - -   \n"
                  "Answer:")
    if guess == answer:
          score = score + 1
          print ("\n Well done!\n"
                 "Your score is", (score),"!\n"
                 "Let's move onto the next question.\n")
                   
    else:
      print ("Incorrect answer, please try again!\n")
      tries = tries + 1

guess = 0
answer = str("£16.23")
tries = 0


while guess != answer and tries <3:
    # put question in quotes below
    guess = input("\n"
                  "  - - - - - - - -   \n"
                  "| Reciept          |\n"
                  "|                  |\n"
                  "| Crisp pack £4.75 |\n"
                  "| Wwine £7.99      |\n"
                  "| Meat      £3.49  |\n"
                  "|                  |\n"
                  "|                  |\n"
                  "|                  |\n"
                  "|                  |\n"
                  "  - - - - - - - -   \n"
                  "Answer:")
    if guess == answer:
          score = score + 1
          print ("\n Well done!\n"
                 "Your score is", (score),"!\n"
                 "Let's move onto the next question.\n")
                   
    else:
      print ("Incorrect answer, please try again!\n")
      tries = tries + 1
if score == 4:
          print("You scored the maximum of 4 points!\n Congratulations!!!")


else:
          print("You scored a total of: ",(score), "Well done!")


    
