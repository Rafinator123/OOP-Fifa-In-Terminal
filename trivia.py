import random
import helper_functions

trivia = [
    ("Which country won the first FIFA World Cup in 1930?", ["Brazil", "Uruguay", "Italy", "Germany"], 1),
    ("Who holds the record for the most goals in World Cup history?", ["Ronaldo", "Pele", "Miroslav Klose", "Gerd Müller"], 2),
    ("Which country has won the most FIFA World Cup titles?", ["Argentina", "Germany", "Italy", "Brazil"], 3),
    ("In what year was the World Cup first broadcast in color?", ["1966", "1970", "1974", "1978"], 1),
    ("Who is the only player to win three World Cups?", ["Pelé", "Maradona", "Zidane", "Beckenbauer"], 0),
    ("Which country hosted the first World Cup held in Africa?", ["Egypt", "Nigeria", "South Africa", "Morocco"], 2),
    ("What is the highest number of goals scored by a team in a single World Cup match?", ["10", "12", "15", "9"], 2),
    ("Who scored the 'Hand of God' goal in the 1986 World Cup?", ["Diego Maradona", "Pelé", "Lionel Messi", "Ronaldo"], 0),
    ("Which nation first introduced the World Cup trophy known as the Jules Rimet Trophy?", ["France", "Brazil", "Italy", "Uruguay"], 0),
    ("Which country won the first ever Women's World Cup in 1991?", ["China", "Germany", "Norway", "United States"], 3),
    ("Who was the youngest player to play in a World Cup?", ["Pelé", "Norman Whiteside", "Lionel Messi", "Michael Owen"], 1),
    ("Which team won the 2014 FIFA World Cup held in Brazil?", ["Spain", "Argentina", "Brazil", "Germany"], 0),
    ("What was unique about the 1950 World Cup final?", ["No final match was played", "It was played indoors", "It was won on penalties", "It featured co-winners"], 0),
    ("Which country has hosted the World Cup the most times?", ["Brazil", "France", "Italy", "Mexico"], 3),
]

def ask_trivia_question():
    # No more questions left
    if not trivia:
        return

    question, options, correct_index = random.choice(trivia)
    trivia.remove((question, options, correct_index))

    print("\n" + question)
    for i, option in enumerate(options):
        print(f"({i + 1}): {option}")

    user_choice = helper_functions.checkValidInputInt(4,1,"Choose your answer: ")

    if int(user_choice) == correct_index:
        print("FUUUUCKKKK YOU GOT IT RIGHT")
        return True
    else:
        #print("Incorrect. The correct answer is:", options[correct_index])
        return False
