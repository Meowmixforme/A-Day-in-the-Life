# James Fothergill Maths Challenge game 12/03/2019

#vars
guess = 0
answer = str("0.25")
tries = 0
score = 0


print ("Welcome to the Maths Challenge")
print ("You have 3 attempts of each question")
print ("Typle decimal answers as 0.11 format ")
print ("")
print ("")
while guess != answer and tries <3:
    guess = input("What is 2 / 8 ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1


guess = 0
answer = str("0.625")
tries = 0

while guess != answer and tries <3:
    guess = input("What is 5 / 8 ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1


guess = 0
answer = str("42")
tries = 0

while guess != answer and tries <3:
    guess = input("What is 7 * 6 ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1

guess = 0
answer = str("2")
tries = 0

while guess != answer and tries <3:
    guess = input("What is 5 -3 ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1




guess = 0
answer = str("12")
tries = 0

while guess != answer and tries <3:
    guess = input("What is 7 + 5 ")
    if guess == answer:
        print ("Correct\n")
        score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1      

guess = 0
answer = str("2")
tries = 0

while guess != answer and tries <3:
    guess = input("Solve -3x-5x=-8-4x ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1

guess = 0
answer = str("10")
tries = 0      

while guess != answer and tries <3:
    guess = input("What is 8 + 2 ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1

guess = 0
answer = str("32")
tries = 0
      
while guess != answer and tries <3:
    guess = input("What is 4 * 8 ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1


print ("Congratulations!! You scored",(score),"out of 24 points")

#Questions taken from Algebra essentials workbook with answers (Chris McMullen,Ph.D.)
    
