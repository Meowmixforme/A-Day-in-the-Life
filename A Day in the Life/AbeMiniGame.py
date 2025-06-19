# name date

#vars
guess = 0
#put answer below
answer = str("39")
tries = 0
score = 0


print ("Welcome to the guess the pattern game 2!")
print ("In this game, you will need to figure out the next number in the pattern listed.")
print ("If you guess corrretly, you'll be awarded 3 points!")
print ("They'll start off easy and get hardy as you go on")
print (" GOOD LUCK!!")
while guess != answer and tries <3:
    # put question in quotes below
    guess = input("Question 1: 4, 6, 14, 18, 24, 31...   ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1


guess = 0
answer = str("37")
tries = 0

while guess != answer and tries <3:
    guess = input("Question 3: 4, 5, 3, 6, 2, 7, 1...   ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1


guess = 0
answer = str("8")
tries = 0

while guess != answer and tries <3:
    guess = input("Question 4: 1, 4, 5, 9, 10, 15, 24...   ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1

guess = 0
answer = str("26")
tries = 0

while guess != answer and tries <3:
    guess = input("Question 5: 1, 8, 27, 64, 125...   ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1




guess = 0
answer = str("216")
tries = 0

while guess != answer and tries <3:
    guess = input("  ")
    if guess == answer:
        print ("Correct\n")
        score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1      




print ("Congratulations!! You scored",(score),"out of 15 points")

#put source weblink here
    
