"""Includes helper functions"""
import random
from pyfiglet import Figlet
from trivia import ask_trivia_question

used_colors = list()

def scoreCalc(offense, defense):
    return max(0, offense - defense)

def calculateGameCPU_group_stages(t1, t2):
    """"""
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

def calculateGameUser_groupStage(t1, t2): 
    t1_score = scoreCalc(random.randint(t1.offense - 2, t1.offense + 2), random.randint(t2.defense - 2, t2.defense + 2))
    t2_score = scoreCalc(random.randint(t2.offense - 2, t2.offense + 2), random.randint(t1.defense - 2 , t1.defense + 2))
    #Go through rounds
    counter = 0
    t1_actual_score = 0
    t2_actual_score = 0
    while counter < t1_score + t2_score:
        #If counter is right
        if counter % 2 == 0:
            #attacking
            print(f"{t1.midfielder} finds {t1.key_outfielder} on the attack! He's through on goal!")
            printTeam(t1,t2)
           
            correct = ask_trivia_question()
            if correct:
                printGoal()
                t1_actual_score += 1
                print("Correct!")
                print(f"Scored by {t1.key_outfielder}")
                print(f"It's {t1.nation} {t1_actual_score} - {t2_actual_score} {t2.nation}")
            else:
                print(f"What a defensive play by {t2.key_defender}...")
                print(f"Score remains {t1.nation} {t1_actual_score} - {t2_actual_score} {t2.nation}")
                t1_score -= 1
        else:
            #defending
            print(f"{t2.midfielder} finds {t2.key_outfielder} on the attack!\n It's all up to {t1.key_defender} to stop it!")
            ask_trivia_question()
            #question generation
            correct = True
            if correct:
                print(f"Scored by {t1.key_outfielder}")
                print(f"It's {t1.nation} {t1_actual_score} - {t2_actual_score} {t2.nation}")
            else:
                t2_actual_score += 1
                print(f"What a defensive play by {t2.key_defender}...")
                print(f"Score remains {t1.nation} {t1_actual_score} - {t2_actual_score} {t2.nation}")
                t2_score -= 1
        print("--------------------------------")
        counter += 1
    print("The referee has blown the wistle...")
    print(f"Final score: {t1.nation} {t1_actual_score} - {t2_actual_score} {t2.nation}")

    if t1_actual_score < t2_actual_score:
        return [t2]
    elif t1_actual_score > t2_actual_score:
        return [t1]
    else:
        return [t1, t2]

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

def printTeam(team1,team2):
    f = Figlet(font='slant')
    print(f.renderText(team1.nation +" vs "+ team2.nation))
