"""Calls main function"""
from pyfiglet import Figlet
import random
import time
from world_cup import WorldCup, Group
from helper_functions import *


#this is for introduction. I.e. each time you run game it will say you had an illustrious carrier at one of these 3
random_soccer_teams = [
    "AC Milan",
    "Juventus FC",
    "Internazionale",
    
    "FC Barcelona",
    "Real Madrid",
    "Atletico de Madrid",

    "Manchester United",
    "Manchester City",
    "Liverpool",
    
    "Bayern Munich",
    "Borussia Dortmund",
]


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

    print(f'''\nAfter an ilustrious career working at {random_soccer_teams[random.randint(0,len(random_soccer_teams)-1)]}, you've been approached 
from the following clubs to manage them at the world cup.\n''')
          
    time.sleep(3)

    ratings=["Easy","Medium","Hard","Very Hard"]
    #Print four teams here going from easy difficulty to hard:
    wc = WorldCup()
    randomized_team_selection =[]
    randomized_team_selection.append(wc.pot1[random.randint(0, len(wc.pot1)-1)])
    randomized_team_selection.append(wc.pot2[random.randint(0, len(wc.pot2)-1)])
    randomized_team_selection.append(wc.pot3[random.randint(0, len(wc.pot3)-1)])
    randomized_team_selection.append(wc.pot4[random.randint(0, len(wc.pot4)-1)])
    
    for i in range(0,4):
        print(f"\n {i + 1}. \n {randomized_team_selection[i].nation}\n--------------\n\
        Challenge Level: {ratings[i]} \nOFFENSE: {stars(randomized_team_selection[i].offense)}\nDEFENSE: {stars(randomized_team_selection[i].defense)}")
        time.sleep(2)
             
    print()
    choice = checkValidInputInt(4,1,"Choose your team: ")
    player_nation = randomized_team_selection[int(choice)-1]
            
    seeOthers = checkValidInputInt(2,1,"\nWould you like to see the results of the other nations? Type 1 for 'YES' and 2 for 'NO': ")
    #Simulate world cup
    #! Group stages
    wc.groupStages()
    if(int(seeOthers)==1):
        wc.printGS()
    #! Round of 16
    
    #!Quarter finals
    
    #!Semi-finals
    
    #!Finals
#main()

printGoal()
