# James Fothergill Menu 05/03/2019

def mainmenu():
    print("1. A Day in the life (Main Game)")
    print("2. James' Maths Quiz 1")
    print("3. James' Maths Quiz 2")
    print("4. James' Guess the number (Easy)")
    print("5. James' Guess the number (Medium)")
    print("6. James' Guess the number (Hard)")
    print("7. James' Binary Game (Easy)")
    print("8. James' Binary Game (Hard)")
    print("9. James' Algebra Game")
    print("10. Abe's Guess the Pattern 1")
    print("11. Abe's Guess the Pattern 2")
    print("12. Ashi's Maths Game")
    print("13. Aqib's Grocery list")
    print("14. Mike's Find the O")
    
    selection=str(input("Enter choice:  "))
    if selection == str(1):
        import ADayInthelifeMainGame
    elif selection == str(2):
        import MathsChallenge
    elif selection == str(3):
        import MathsChallenge2       
    elif selection == str(4):
        import guesseasy
    elif selection == str(5):
        import guessmedium
    elif selection == str(6):
        import guesshard
    elif selection ==str(7):
        import Binaryeasy
    elif selection ==str(8):
        import Binaryhard
    elif selection ==str(9):
        import AlgebraJamesMiniGame
    elif selection ==str(10):
        import pattern
    elif selection ==str(11):
        import AbeMiniGame
    elif selection ==str(12):
        import AshiMiniGame
    elif selection ==str(13):
        import AqibMiniGame
    elif selection ==str(14):
        import AndMikeMiniGame
        
    else:
        print("Invalid choice. Enter 1-14")
        mainmenu()



mainmenu()









