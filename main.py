"""Calls main function"""
from pyfiglet import Figlet
import random
import time
from world_cup import WorldCup, Group
import trivia
from helper_functions import calculateGameCPU_group_stages


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
    f_name = input("What is your first name? ")
    l_name = input("What is your last name? ")
    print("Coach's Name:",f_name,l_name)

    print(f'''\nAfter an ilustrious career working at {random_soccer_teams[random.randint(0,len(random_soccer_teams)-1)]}, you've been approached 
from the following clubs to manage them at the world cup.\n''')
          
    time.sleep(2)

    ratings=["Easy","Medium","Hard","Very Hard"]
    # Print four teams here going from easy difficulty to hard:
    wc = WorldCup()
    randomized_team_selection =[]
    randomized_team_selection.append(wc.pot1[random.randint(0, len(wc.pot1)-1)])
    randomized_team_selection.append(wc.pot2[random.randint(0, len(wc.pot2)-1)])
    randomized_team_selection.append(wc.pot3[random.randint(0, len(wc.pot3)-1)])
    randomized_team_selection.append(wc.pot4[random.randint(0, len(wc.pot4)-1)])
    
    for i in range(0,4):
        print(f"({i + 1}): {randomized_team_selection[i].nation:<20} Challenge Level: {ratings[i]:<10} OFFENSE: {randomized_team_selection[i].offense:<10} DEFENSE: {randomized_team_selection[i].defense}")
        time.sleep(1)      
    
    print()
    
    #validate input 
    while True:
        print("Choose your team: ")
        choice = input()
        if (isNum(choice) and int(choice) > 0 and int(choice) < 5):
            player_nation = randomized_team_selection[int(choice)-1]
            break
    
    print(f"\nYou have chosen {player_nation.nation} as your team. Good luck!")


    # Demo of trivia questions
    trivia.ask_trivia_question()
    trivia.ask_trivia_question()
    trivia.ask_trivia_question()

    #Simulate world cup
    #! Group stages
    wc.groupStages()
    #! Round of 16
    #!Quarter finals
    #!Semi-finals
    #!Finals
main()
