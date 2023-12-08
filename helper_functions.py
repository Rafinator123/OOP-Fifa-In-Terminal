"""Includes helper functions"""
import random
from pyfiglet import Figlet

used_colors = list()

def scoreCalc(offense, defense):
    return max(0, offense - defense)

def calculateGameCPU_group_stages(t1, t2):
    t1_score = scoreCalc(random.randint(t1.offense-2,t1.offense+2), random.randint(t2.defense-2, t2.offense+2))
    t2_score = scoreCalc(random.randint(t2.offense-2,t2.offense+2), random.randint(t1.defense-2, t1.offense+2))
    if t1_score == t2_score: 
        return [t1,t2]
    elif t1_score > t2_score: 
        return [t1]
    else:
        return [t2]
    
def calculateGameCPU_knockouts(t1, t2):
    """Calculates games between teams"""
    
    t1_score = scoreCalc(random.randint(t1.offense-2,t1.offense+2), random.randint(t2.defense-2, t2.offense+2))
    t2_score = scoreCalc(random.randint(t2.offense-2,t2.offense+2), random.randint(t1.defense-2, t1.offense+2))
    #Extra time
    if t1_score == t2_score:
        t1_score = scoreCalc(random.randint(t1.offense-2,t1.offense), random.randint(t2.defense-2, t2.offense))
        t2_score = scoreCalc(random.randint(t2.offense-2,t2.offense), random.randint(t1.defense-2, t1.offense))
        if t1_score > t2_score:
            return t1
        elif t1_score < t2_score:
            return t2
    else:
        if t1_score > t2_score:
            return t1
        else:
            return t2
    # Penalties
    t1_penalties = 0
    t2_penalties = 0

    while t1_penalties < 5 and t2_penalties < 5:
        t1_penalty_score = random.randint(0, 1)
        t2_penalty_score = random.randint(0, 1)

        if t1_penalty_score > t2_penalty_score:
            t1_penalties += 1
        else:
            t2_penalties += 1

    if t1_penalties > t2_penalties:
        return t1
    else:
        return t2

def calculateGameUser(opposition): 
    """Calculates game between user and opposition"""
    return

def generateQuestion():
    """Returns question:answer paring."""
    return

def stars(num_starz):
    return '* '*num_starz

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
        if len(out)>0 and isNum(out) and int(out)<=upperLim and int(out)>=lowerLim:
            loop=False
            return out
        else:
            print("Invalid Input, try again")

def printGoal():
    f = Figlet(font='slant')
    print(f.renderText('GOAL!!!'))
