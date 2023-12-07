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
    if len(inp)==0: return False
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
    
    print()
    checkValidInputInt(4,1,"Choose a team: ")
    print("\nCurrent Lineup:\n--------------\nCoach:",f_name,l_name+"\n--------------")
    positions = ["GK","LB","CB","CB","RB","CM","CM","CAM","LW","ST","RW"]
    for i in positions:
        print(i+":",names.get_full_name(gender="male"))
        time.sleep(.25)




main()