# name date

#vars
guess = 0
#put answer below
answer = str("(-5x-6)")
tries = 0
score = 0


print ("Welcome to the ")
print ("You have 3 attempts of each question")
print ("The format of these questions will be: 'C(N+M)', ")
print ("")
print ("")
while guess != answer and tries <3:
    # put question in quotes below
    guess = input("Remove the brackets in the following expressions: -5(1+x)+(2-3)\n")
    if guess == answer:
          print ("Correct\n")
          score = score + 1          
    else:
      print ("Incorrect")
      tries = tries + 1


guess = 0
answer = str("(10ax+15ab-20ac)")
tries = 0

while guess != answer and tries <3:
    guess = input("Remove the brackets in the following expressions: 5a(2x+3b-4c)\n")
    if guess == answer:
          print ("Correct\n")
          score = score + 1         
    else:
      print ("Incorrect")
      tries = tries + 1


guess = 0
answer = str("(x=-6)")
tries = 0

while guess != answer and tries <3:
    guess = input("solve the equations: 2x+9=x+3\n")
    if guess == answer:
          print ("Correct\n")
          score = score + 1          
    else:
      print ("Incorrect")
      tries = tries + 1

guess = 0
answer = str("x=3")
tries = 0

while guess != answer and tries <3:
    guess = input("solve the following linear equations: 8x-2x+3=3x+12\n")
    if guess == answer:
          print ("Correct\n")
          score = score + 1          
    else:
      print ("Incorrect")
      tries = tries + 1




guess = 0
answer = str("x=4")
tries = 0

while guess != answer and tries <3:
    guess = input("solve the following linear equations: 4x-6=3x+10\n")
    if guess == answer:
        print ("Correct\n")
        score = score + 1          
    else:
      print ("Incorrect")
      tries = tries + 1      

guess = 0
answer = str("x=4")
tries = 0

while guess != answer and tries <3:
    guess = input("solve the following linear quations: 15-2x=7\n")
    if guess == answer:
          print ("Correct\n")
          score = score + 1          
    else:
      print ("Incorrect")
      tries = tries + 1

guess = 0
answer = str("x=9,y=1")
tries = 0      

while guess != answer and tries <3:
    guess = input("solve the following simultaneous linear equations by elimination: 4x-2y=34;x+3y=12\n")
    if guess == answer:
          print ("Correct\n")
          score = score + 1          
    else:
      print ("Incorrect")
      tries = tries + 1

guess = 0
answer = str("x=0,y=5")
tries = 0
      
while guess != answer and tries <3:
    guess = input("solve the following simultaneous linear equations by elimination: 3x-y=-5;-7x=3y=15\n")
    if guess == answer:
          print ("Correct\n")
          score = score + 1          
    else:
      print ("Incorrect")
      tries = tries + 1


print ("Congratulations!! You scored",(score),"out of 8 points")

#put source weblink here
    
