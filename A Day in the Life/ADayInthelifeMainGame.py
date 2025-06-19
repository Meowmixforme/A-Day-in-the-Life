#A day in the life James Fothergill 27/02/2019

import Title
#vars
name = input("What is your Name? ")
score = 0




#Into 
def intro():
    print ("")
    print ("Welcome to A Day in The Life.")
    print ("The objective of this game is to test your maths skills as a Computer Science student and prepare you for the first maths exam.")
    print ("Throughout the game you will be given the opportunity to gain intelligence (INT) points from your choices,")
    print ("These choices will determine the difficulty of the final exam.")
    print ("The player will have the option to skip mini-games by choosing answers that reflect a bad study ethic.")
    print ("If the player wishes to really be challenged, it is suggested to collect as many INT points as possible and take the harder exam.")
    print ("")
    print ("")

def details():
    print ("Light filters through your blinds as you wake with a pounding headache and the sound of loud ringing.")
    print ("You reach your arm over and press snooze on your alarm.")
    print ("You remember that you went out last night drinking to calm pre-test nerves, though you don’t remember much else.")
    print (("You reach over to a notepad on your your desk, there is a name on the notepad."),(name),("!"))
    print ("")
    print ("")

def scn1():
    global score
    playerchoice = 0
    print ("You remember that you must catch the train to Teesside University in an hour, otherwise you’ll be late.")
    print ("The bed feels so warm and cosy that you don’t want to get up. Your alarm sounds for a second time.")
    print (("What do you do"),(name),("?"))
    print ("")
    print ("")
    print ("1.Get out of bed, have a coffee to wake yourself up and attend the lecture.")
    print ("2.Get up, don't attend the lecture but read the lecture slides and watch the YouTube videos posted by your lecturer.")
    print ("3.Press the snooze button on your alarm and don't attend the lecture or read the slides.")
    while playerchoice != True:
     playerchoice = input("Enter Choice:  1, 2 or 3 ")
     if playerchoice == str(1) :
      score = score + 3
      playerchoice = True
     elif playerchoice == str(2) :
      score = score + 2
      playerchoice = True
     elif playerchoice == str(3) :
      score = score + 1
      playerchoice = True
     else: print("Please choose 1, 2 or 3") 

    

def scn2():
    global score
    playerchoice = 0
    print ("")
    print ("")
    print ("You decide to spend some time in the library in order to practise your arithmetic.")
    print ("Upon leaving your current location you discover that it is raining heavily outside.")
    print (("What do you do"),(name),("?"))
    print ("")
    print ("")
    print ("1.Decide that it’s not worth getting wet and abandon your studies.")
    print ("2.Run across the campus to the library, getting your clothes all wet and take a maths challenge.")
    print ("3.Try and practise arithmatic using the internet on your iPad.")
    while playerchoice != True:
     playerchoice = input("Enter Choice:  1, 2 or 3 ")
     if playerchoice == str(1) :
      score = score + 1
      playerchoice = True
      import guessmedium
     elif playerchoice == str(2) :
      score = score + 3
      playerchoice = True
      import MathsChallenge
     elif playerchoice == str(3) :
      score = score + 1
      playerchoice = True
      import guesshard
     else: print("Please choose 1, 2 or 3")
     


    
def scn3():
    global score
    playerchoice = 0
    print ("")
    print ("")
    print ("You arrive at your usual lecture room to take a Algebra test only to find that no one is there, and your iPad won’t connect to the internet.")
    print ("On leaving the building you notice a friend who takes the same class walking and go over to talk.")
    print (("What do you do"),(name),("?"))
    print ("")
    print ("")
    print ("1.Take a maths quiz on your ipad with your friend and grab a coffee, forgetting all about the lecture.")
    print ("2.Send an email to the lecturer and other students in the hope that someone will respond and guide you to the correct room.")
    print ("3.Ask your friend if they know which room the lecture was changed to or if they can check their iPad to find out and take.")
    while playerchoice != True:
     playerchoice = input("Enter Choice:  1, 2 or 3 ")
     if playerchoice == str(1) :
      score = score + 2
      playerchoice = True
      import Ashi
     elif playerchoice == str(2) :
      score = score + 1
      playerchoice = True
      import guesseasy
     elif playerchoice == str(3) :
      score = score + 3
      playerchoice = True
      import algebra
    else: print("Please choose 1, 2 or 3")  

def scn4():
    global score
    playerchoice = 0
    print ("Lunchtime comes around and you've been working hard all day.")
    print ("You are hungry but could also brush up on more studying.")
    print (("What do you do"),(name),("?"))
    print ("")
    print ("")
    print ("1.Go to the shops while you have time and buy groceries.")
    print ("2.Study math patterns at the library and go hungry.")
    print ("3.Go eat and avoid studies.")
    playerchoice =int(input("Enter Choice:  "))
    while playerchoice != True:
     playerchoice = input("Enter Choice:  1, 2 or 3 ")
     if playerchoice == str(1) :
      score = score + 2
      playerchoice = True
      import grocery
     elif playerchoice == str(2) :
      score = score + 3
      playerchoice = True
      import pattern
     elif playerchoice == str(3) :
      score = score + 2
      playerchoice = True
      import guesshard3
    else: print("Please choose 1, 2 or 3")

def scn5():
    global score
    playerchoice = 0
    print ("Your lecturer Pete Dwyer surprises the whole class with a pre- exam Maths Challenge.")
    print ("")
    print (("What do you do"),(name),("?"))
    print ("")
    print ("")
    print ("1.Go into the library and take a guess the pattern quiz.")
    print ("2.Go into the library and learn some graphing online.")
    print ("3.Go into the study room and take Pete Dwyer's Maths Challenge.")
    playerchoice =int(input("Enter Choice:  "))
    while playerchoice != True:
     playerchoice = input("Enter Choice:  1, 2 or 3 ")
     if playerchoice == str(1) :
      score = score + 2
      playerchoice = True
      import patternv2
     elif playerchoice == str(2) :
      score = score + 2
      playerchoice = True
      import Mike
     elif playerchoice == str(3) :
      score = score + 3
      playerchoice = True
      import MathsChallenge2
    else: print("Please choose 1, 2 or 3")    
    
def end():
    global score
    print ("")
    print ("")
    print("Congratualations! You Scored",(score))
    print ("")
    print ("")
    if score >=10:
     import Binaryhard

    if score <=10:
        import Binaryeasy

  
intro()

details()

scn1()

scn2()

scn3()

scn4()

scn5()

end()

    





#An overview of how to code an adventure game = https://www.techradar.com/how-to/computing/how-to-code-your-own-adventure-game-in-python-1313296
# for bat file https://stackoverflow.com/questions/3591807/how-can-i-stop-python-exe-from-closing-immediately-after-i-get-an-output


