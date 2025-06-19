# 13/032019 Mike Pitchers Ashiqul Islam

#vars
guess = 0
#put answer below
answer = str("12")
tries = 0
score = 0


print ("Welcome to the second Maths Challenge")
print ("You have 3 attempts of each question")
print ("Typle decimal answers as 0.11 format ")
print ("")
print ("")
while guess != answer and tries <3:
    # put question in quotes below
    guess = input("What is 10 + 2?: ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1


guess = 0
answer = str("804")
tries = 0

while guess != answer and tries <3:
    guess = input("What is 402 x 4 / 2?:  ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1


guess = 0
answer = str("60")
tries = 0

while guess != answer and tries <3:
    guess = input("What is 6 x 10?:  ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1

guess = 0
answer = str("4")
tries = 0

while guess != answer and tries <3:
    guess = input("What is the square root of 16?: ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1




guess = 0
answer = str("72")
tries = 0

while guess != answer and tries <3:
    guess = input("What is 9 x 8?: ")
    if guess == answer:
        print ("Correct\n")
        score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1      

guess = 0
answer = str("26 ")
tries = 0

while guess != answer and tries <3:
    guess = input("what is 78 - 52?:  ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1

guess = 0
answer = str("48")
tries = 0      

while guess != answer and tries <3:
    guess = input(" what is 2304 / 48?: ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1

guess = 0
answer = str("270")
tries = 0
      
while guess != answer and tries <3:
    guess = input("what is 540 * 2 / 4?:  ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1


print ("Congratulations!! You scored",(score),"out of 24 points")

#put source weblink here
    
