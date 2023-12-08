"""App file containing class definitions"""
from helper_functions import calculateGameCPU_group_stages

class Nation:
    def __init__(self, c: str, n: str, o: str, mid : str, d: str, off, deff: str) -> None:
        self.coach = c
        self.nation = n
        self.key_outfielder = o
        self.key_defender = d
        self.offense = off
        self.midfielder = mid
        self.defense = deff
        pass
        
class Group:
    """Class containing each group where group has 4 nations that will play against each other"""
    def __init__(self, l, n1,n2,n3,n4) -> None:
        self.letter = l
        self.group = {}
        self.group["a"] = [n1,0]
        self.group["b"] = [n2,0]
        self.group["c"] = [n3,0]
        self.group["d"] = [n4,0]
        return
    def simulateGroupStage(self):
        def getPoints(t1, t2):
            winner = calculateGameCPU_group_stages(self.group[t1][0], self.group[t2][0])
            if len(winner) > 1:
                self.group[t1][1] += 1
                self.group[t2][1] += 1
            else:
                if winner == t1:
                    self.group[t1][1] += 3
                else:
                    self.group[t2][1] += 3
        """Simulaes games for the whole group."""
        #First round
        getPoints("a","b")
        getPoints("c","d")
        #Second round
        getPoints("a","d")
        getPoints("b","c")
        #third round
        getPoints("a","c")
        getPoints("b", "d")
    
    def printOutTable(self):
        print(f"Group {self.letter}\n ------------------ \n ")
        
        # Sort nations in the group based on points
        sorted_nations = sorted(self.group.values(), key=lambda x: x[1], reverse=True)

        for i, (nation, points) in enumerate(sorted_nations, start=1):
            print(f"{i}. {nation.nation} - Points: {points}")
        
class WorldCup:
    def __init__(self):
        self.groups = []
        self.pot1 =[]
        self.pot2 =[]
        self.pot3 =[]
        self.pot4 = []
        # Group A
        qatar = Nation("Félix Sánchez Bas", "Qatar", "Akram Afif", "Boualem Khoukhi", "Bassam Al-Rawi", 1, 1)
        ecuador = Nation("Gustavo Alfaro", "Ecuador", "Enner Valencia", "Carlos Gruezo", "Piero Hincapié", 3, 3)
        senegal = Nation("Aliou Cissé", "Senegal", "Sadio Mané", "Idrissa Gueye", "Kalidou Koulibaly", 4, 3)
        netherlands = Nation("Louis van Gaal", "Netherlands", "Memphis Depay", "Frenkie de Jong", "Virgil van Dijk", 5, 5)
        groupA = Group("A",qatar, ecuador, senegal, netherlands)
        self.pot1.append(netherlands)
        self.pot2.append(senegal)
        self.pot3.append(ecuador)
        self.pot4.append(qatar)
        self.groups.append(groupA)
        # Group B
        england = Nation("Gareth Southgate", "England", "Harry Kane", "Jude Bellingham", "Harry Maguire", 5, 5)
        iran = Nation("Dragan Skočić", "Iran", "Sardar Azmoun", "Alireza Jahanbakhsh", "Milad Mohammadi", 3, 2)
        usa = Nation("Gregg Berhalter", "USA", "Christian Pulisic", "Weston McKennie", "John Brooks", 3, 3)
        wales = Nation("Rob Page", "Wales", "Gareth Bale", "Aaron Ramsey", "Joe Rodon", 3, 2)
        groupB = Group("B",england, iran, usa, wales)
        self.pot1.append(england)
        self.pot2.append(usa)
        self.pot3.append(wales)
        self.pot4.append(iran)
        self.groups.append(groupB)
        
        # Group C
        argentina = Nation("Lionel Scaloni", "Argentina", "Lionel Messi", "Alexis MacAllister", "Emiliano Martínez", 5, 5)
        saudi_arabia = Nation("Hervé Renard", "Saudi Arabia", "Salem Al-Dawsari", "Abdullah Otayf", "Yasser Al-Shahrani", 2, 2)
        mexico = Nation("Gerardo Martino", "Mexico", "Raúl Jiménez", "Héctor Herrera", "Guillermo Ochoa", 4, 4)
        poland = Nation("Paulo Sousa", "Poland", "Robert Lewandowski", "Grzegorz Krychowiak", "Kamil Glik", 4, 3)
        groupC = Group("C",argentina, saudi_arabia, mexico, poland)
        self.pot1.append(argentina)
        self.pot2.append(mexico)
        self.pot3.append(poland)
        self.pot4.append(saudi_arabia)
        self.groups.append(groupC)
        
        # Group D
        france = Nation("Didier Deschamps", "France", "Kylian Mbappé", "Antoine Griezmann", "Raphael Varane", 5, 5)
        australia = Nation("Graham Arnold", "Australia", "Mat Ryan", "Aaron Mooy", "Mathew Leckie", 3, 3)
        denmark = Nation("Kasper Hjulmand", "Denmark", "Christian Eriksen", "Pierre-Emile Højbjerg", "Simon Kjaer", 4, 4)
        tunisia = Nation("Mondher Kebaier", "Tunisia", "Youssef Msakni", "Wahbi Khazri", "Dylan Bronn", 2, 1)
        groupD = Group("D",france, australia, denmark, tunisia)
        self.pot1.append(france)
        self.pot2.append(denmark)
        self.pot3.append(australia)
        self.pot4.append(tunisia)
        self.groups.append(groupD)
        
        # Group E
        spain = Nation("Luis Enrique", "Spain", "Álvaro Morata", "Sergio Busquets", "Pau Torres", 5, 5)
        costa_rica = Nation("Luis Fernando Suárez", "Costa Rica", "Joel Campbell", "Bryan Ruiz", "Keylor Navas", 3, 3)
        germany = Nation("Hansi Flick", "Germany", "Thomas Müller", "Leon Goretzka", "Mauel Neuer", 4, 4)
        japan = Nation("Hajime Moriyasu", "Japan", "Takefusa Kubo", "Gaku Shibasaki", "Maya Yoshida", 4, 3)
        groupE = Group("E",spain, costa_rica, germany, japan)
        self.pot1.append(spain)
        self.pot2.append(germany)
        self.pot3.append(japan)
        self.pot4.append(costa_rica)
        self.groups.append(groupE)
        
        # Group F
        belgium = Nation("Roberto Martínez", "Belgium", "Romelu Lukaku", "Kevin De Bruyne", "Thibaut Courtois", 5, 5)
        canada = Nation("John Herdman", "Canada", "Jonathan David", "Scott Arfield", "Alphonso Davies", 2, 3)
        morocco = Nation("Vahid Halilhodžić", "Morocco", "Achraf Hakimi", "Hakim Ziyech", "Romain Saïss", 3, 4)
        croatia = Nation("Zlatko Dalić", "Croatia", "Ivan Perišić", "Luka Modrić", "Domagoj Vida", 4, 4)
        groupF = Group("F",belgium, canada, morocco, croatia)
        self.pot1.append(belgium)
        self.pot2.append(croatia)
        self.pot3.append(morocco)
        self.pot4.append(canada)
        self.groups.append(groupF)
        
        # Group G
        brazil = Nation("Tite (Adenor Leonardo Bacchi)", "Brazil", "Neymar Jr.", "Casemiro", "Marquinhos", 5, 5)
        serbia = Nation("Dragan Stojković", "Serbia", "Dušan Tadić", "Sergej Milinković-Savić", "Aleksandar Kolarov", 3, 4)
        switzerland = Nation("Murat Yakin", "Switzerland",  "Xherdan Shaqiri", "Granit Xhaka","Manuel Akanji", 3, 3)
        cameroon = Nation("Toni Conceição", "Cameroon", "Eric Maxim Choupo-Moting", "André-Frank Zambo Anguissa", "Joël Matip", 4, 2)
        groupG = Group("G",brazil, serbia, switzerland, cameroon)
        self.pot1.append(brazil)
        self.pot2.append(serbia)
        self.pot3.append(switzerland)
        self.pot4.append(cameroon)
        self.groups.append(groupG)
        
        # Group H
        portugal = Nation("Fernando Santos", "Portugal", "Cristiano Ronaldo", "Bruno Fernandes", "Ruben Dias", 5, 5)
        ghana = Nation("Otto Addo", "Ghana", "Andre Ayew", "Thomas Partey", "Daniel Amartey", 3, 3)
        uruguay = Nation("Óscar Tabárez", "Uruguay", "Luis Suárez", "Federico Valverde", "José María Giménez", 4, 4)
        korea_republic = Nation("Paulo Bento", "Korea Republic", "Son Heung-min", "Hwang Hee-chan", "Kim Min-jae", 2, 2)
        groupH = Group("H",portugal, ghana, uruguay, korea_republic)
        self.pot1.append(portugal)
        self.pot2.append(uruguay)
        self.pot3.append(ghana)
        self.pot4.append(korea_republic)
        self.groups.append(groupH)
        
    def groupStages(self):
        for i in range(0, len(self.groups)):
            self.groups[i].simulateGroupStage()

    def printGS(self):
        for i in range(0, len(self.groups)):
            self.groups[i].printOutTable()

    def simulate(self):
        self.groupStages()
        self.quarterFinals()
        self.semiFinals()
        self.finals()
        return
        