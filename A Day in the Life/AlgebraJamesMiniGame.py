# James Fothergill Algebra game 11/03/2019

#vars
guess = 0
answer = str("-17/2")
tries = 0
score = 0


print ("Welcome to the Algebra test")
print ("You have 3 attempts of each question")
print ("for fractional answers give num/num\n")
print ("")
print ("")
while guess != answer and tries <3:
    guess = input("Solve 9-2x=-8-4x ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1


guess = 0
answer = str("-1")
tries = 0

while guess != answer and tries <3:
    guess = input("Solve 9+8x=5x+6 ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1


guess = 0
answer = str("-2/7")
tries = 0

while guess != answer and tries <3:
    guess = input("Solve 2x+5x=-2 ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1

guess = 0
answer = str("-2")
tries = 0

while guess != answer and tries <3:
    guess = input("Solve -3x-8=-x-4 ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1




guess = 0
answer = str("1/14")
tries = 0

while guess != answer and tries <3:
    guess = input("Solve 9x-1=-5 ")
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
answer = str("-1/5")
tries = 0      

while guess != answer and tries <3:
    guess = input("Solve -3+4x=-5-6x ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1

guess = 0
answer = str("3")
tries = 0
      
while guess != answer and tries <3:
    guess = input("Solve 2x+6=5x-x ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1


print ("Congratulations!! You scored",(score),"out of 24 points")

#Questions taken from Algebra essentials workbook with answers (Chris McMullen,Ph.D.)
    
