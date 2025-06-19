#Binary game Hard James fothergill 09/03/2019

#vars
guess = 0
answer = str(545)
tries = 0
score = 0


print ("Welcome to the Hard binary test")
print ("You have 3 attempts of each question")
print ("The maximum grade for this test is A\n")

while guess != answer and tries <3:
    guess = input("Convert 2305 (Base 6) to denary (Base 10)  ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1


guess = 0
answer = str(2417)
tries = 0

while guess != answer and tries <3:
    guess = input("Convert 1295 Base10 to Base 8:  ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1


guess = 0
answer = str(1111011)
tries = 0

while guess != answer and tries <3:
    guess = input("Convert 123 to binary:  ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1

guess = 0
answer = str(173)
tries = 0

while guess != answer and tries <3:
    guess = input("Convert 10101101(Base2) to denary (Base10):  ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1




guess = 0
answer = str(1010101100100111)
tries = 0

while guess != answer and tries <3:
    guess = input("AB27(HEX) to binary:  ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1      

guess = 0
answer = str(10110)
tries = 0

while guess != answer and tries <3:
    guess = input("Add 1011 to 1011):  ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1

guess = 0
answer = str(10110.00111101)
tries = 0      

while guess != answer and tries <3:
    guess = input("Convert 11.24 (Base10) to Binary:  ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1

guess = 0
answer = str(231)
tries = 0
      
while guess != answer and tries <3:
    guess = input("Convert 11100111 (Binary) to Base10:  ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1


guess = 0
answer = str(70)
tries = 0

while guess != answer and tries <3:
    guess = input("Convert 64 (Base10) to Base9:  ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1

guess = 0
answer = str(14)
tries = 0      

while guess != answer and tries <3:
    guess = input("Convert 1001(Binary) to Base 5:  ")
    if guess == answer:
          print ("Correct\n")
          score = score + 3          
    else:
      print ("Incorrect")
      tries = tries + 1
      



if score >= 30:
    print ("Congratulations, you scored a A with" , (score))
elif score >=20:
    print ("Congratulations, you scored an B with" , (score))
elif score >=10:
    print ("Congratulations, you scored an C with" , (score))
elif score >=5:
    print ("You Failed with a score of" , (score))
elif score ==0:
    print ("No Score")    









#https://www.youtube.com/watch?v=5mbmWb7_KgU
