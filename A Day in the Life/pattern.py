# name date

#vars
guess = 0
#put answer below
answer = str("37")
tries = 0
score = 0


print ("Welcome to the guess the pattern game!")
print ("In this game, you will need to figure out the next number in the pattern listed.")
print ("If you guess corrretly, you'll be awarded 3 points!")
print (" GOOD LUCK!!")
print ("")
print ("")
while guess != answer and tries <3:
    # put question in quotes below
    guess = input("17, 19, 23, 29, 31... ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1





print ("Congratulations!! You scored",(score),"out of 3 points")

#put source weblink here
    
