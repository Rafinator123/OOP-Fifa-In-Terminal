"""Calls main function"""
from pyfiglet import Figlet
import random
import names
import time

#this is for introduction. I.e. each time you run game it will say you had an illustrious carrier at one of these 3
random_soccer_teams = [
    "FC Barcelona",
    "Manchester United FC",
    "Juventus FC",
    "Bayern Munich",
    "Paris Saint-Germain FC",
    "Boca Juniors",
    "Ajax Amsterdam",
    "Flamengo",
    "Borussia Dortmund",
    "Celtic FC"
]


def isNum(inp):
    for i in inp:
        if not i.isdigit():
            return False
    return True


def checkValidInputInt(upperLim,lowerLim,inputQuestion):
    #upper lim and lower lim are INCLUSIVE
    loop=True
    while(loop):
        out=input(inputQuestion)
        if isNum(out) and int(out)<=upperLim and int(out)>=lowerLim:
            loop=False
            return out
        else:
            print("Invalid Input, try again")


def main():
    print("----------------------------------------------------------------------------------")
    f = Figlet(font='slant')
    print(f.renderText('Welcome to PyFIFA!'))
    print("----------------------------------------------------------------------------------")
    print('''
PyFIFA is an interactive text-based soccer game inspired by the 2023 FIFA World 
Cup in Qatar. Please press the Enter/Return button on your keyboard to start the 
game and initate character creation. We hope you enjoy!

This package was created by:
Alex Hmitti
Rafael-Nadal Scala
Aaron Stein

Github:
https://github.com/Rafinator123/OOP-Fifa-In-Terminal
''')
    print("----------------------------------------------------------------------------------")
    input() #waits for user to click 
    print("Character Creation:")
    f_name = input("What is your first name? ")
    l_name = input("What is your last name? ")
    print("Coach's Name:",f_name,l_name)

    print(f'''\nAfter an ilustrious career working at {random_soccer_teams[random.randint(0,9)]}, you've been approached 
from the following clubs to manage them at the world cup.\n''')
          
    time.sleep(3)

    ratings=["Easy","Medium","Hard","Very Hard"]
    #Print four teams here going from easy difficulty to hard:
    for i in range(1,5,1):
        print("\n"+str(i)+".\nTEAM NAME\n"+"--------------\nChallenge Level:",ratings[i-1],"\nOFFENSE: [stars here]\nDEFENSE: [stars here]")
        time.sleep(2)      
    
    print()
    checkValidInputInt(4,1,"Choose a team: ")
    print("\nCurrent Lineup:\n--------------\nCoach:",f_name,l_name+"\n--------------")
    positions = ["GK","LB","CB","CB","RB","CM","CM","CAM","LW","ST","RW"]
    for i in positions:
        print(i+":",names.get_full_name(gender="male"))






main()

