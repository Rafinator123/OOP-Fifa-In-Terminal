"""App file containing class definitions"""
from helper_functions import *

class Nation:
    def __init__(self, c: str, n: str, o: str, mid : str, d: str, off, deff) -> None:
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
    def __init__(self, n1,n2,n3,n4) -> None:
        self.group["a"] = [n1,0]
        self.group["b"] = [n2,0]
        self.group["c"] = [n3,0]
        self.group["d"] = [n4,0]
        return
    def simulateGamesCPU(self):
        """Simulaes games for the whole group."""
        #First round
        winner =calculateGameCPU(self.group["a"][1], self.group["b"][1])
        self.group[winner][1] += 3
        winner = calculateGameCPU(self.group["c"[1]], self.group["d"][1])
        self.group[winner][1] += 3
        #Second round
        winner = calculateGameCPU(self.group["b"][1], self.group["c"][1])
        self.group[winner][1] += 3
        winner = calculateGameCPU(self.group["a"][1], self.group["d"][1])
        self.group[winner][1] += 3
        #third round
        winner = calculateGameCPU(self.group["a"][1], self.group["c"][1])
        self.group[winner][1] += 3
        winner = calculateGameCPU(self.group["b"][1], self.group["d"][1])
        self.group[winner][1] += 3
        
        
        
class WorldCup:
    def __init__(self):
        self.groups = []
        # Group A
        qatar = Nation("Félix Sánchez Bas", "Qatar", "Akram Afif", "Boualem Khoukhi", "Bassam Al-Rawi", 1.5, 1)
        ecuador = Nation("Gustavo Alfaro", "Ecuador", "Enner Valencia", "Carlos Gruezo", "Piero Hincapié", 3.5, 3)
        senegal = Nation("Aliou Cissé", "Senegal", "Sadio Mané", "Idrissa Gueye", "Kalidou Koulibaly", 4, 3.5)
        netherlands = Nation("Louis van Gaal", "Netherlands", "Memphis Depay", "Frenkie de Jong", "Virgil van Dijk", 4.5, 4.5)
        groupA = Group(qatar, ecuador, senegal, netherlands)
        self.groups.append(groupA)
        # Group B
        england = Nation("Gareth Southgate", "England", "Harry Kane", "Jude Bellingham", "Harry Maguire", 5, 4.5)
        iran = Nation("Dragan Skočić", "Iran", "Sardar Azmoun", "Alireza Jahanbakhsh", "Milad Mohammadi", 3, 2)
        usa = Nation("Gregg Berhalter", "USA", "Christian Pulisic", "Weston McKennie", "John Brooks", 3.5, 3)
        wales = Nation("Rob Page", "Wales", "Gareth Bale", "Aaron Ramsey", "Joe Rodon", 3, 2.5)
        groupB = Group(england, iran, usa, wales)
        self.groups.append(groupB)
        
        # Group C
        argentina = Nation("Lionel Scaloni", "Argentina", "Lionel Messi", "Alexis MacAllister", "Emiliano Martínez", 5, 4.5)
        saudi_arabia = Nation("Hervé Renard", "Saudi Arabia", "Salem Al-Dawsari", "Abdullah Otayf", "Yasser Al-Shahrani", 2.5, 2)
        mexico = Nation("Gerardo Martino", "Mexico", "Raúl Jiménez", "Héctor Herrera", "Guillermo Ochoa", 4, 4)
        poland = Nation("Paulo Sousa", "Poland", "Robert Lewandowski", "Grzegorz Krychowiak", "Kamil Glik", 4, 3.5)
        groupC = Group(argentina, saudi_arabia, mexico, poland)
        self.groups.append(groupC)
        
        # Group D
        france = Nation("Didier Deschamps", "France", "Kylian Mbappé", "Antoine Griezmann", "Raphael Varane", 5, 5)
        australia = Nation("Graham Arnold", "Australia", "Mat Ryan", "Aaron Mooy", "Mathew Leckie", 3.5, 3.5)
        denmark = Nation("Kasper Hjulmand", "Denmark", "Christian Eriksen", "Pierre-Emile Højbjerg", "Simon Kjaer", 4, 4)
        tunisia = Nation("Mondher Kebaier", "Tunisia", "Youssef Msakni", "Wahbi Khazri", "Dylan Bronn", 2, 1.5)
        groupD = Group(france, australia, denmark, tunisia)
        self.groups.append(groupD)
        
        # Group E
        spain = Nation("Luis Enrique", "Spain", "Álvaro Morata", "Sergio Busquets", "Pau Torres", 4.5, 4.5)
        costa_rica = Nation("Luis Fernando Suárez", "Costa Rica", "Joel Campbell", "Bryan Ruiz", "Keylor Navas", 3, 3)
        germany = Nation("Hansi Flick", "Germany", "Thomas Müller", "Leon Goretzka", "Mauel Neuer", 4, 4)
        japan = Nation("Hajime Moriyasu", "Japan", "Takefusa Kubo", "Gaku Shibasaki", "Maya Yoshida", 4, 3.5)
        groupE = Group(spain, costa_rica, germany, japan)
        self.groups.append(groupE)
        
        # Group F
        belgium = Nation("Roberto Martínez", "Belgium", "Romelu Lukaku", "Kevin De Bruyne", "Thibaut Courtois", 4.5, 4.5)
        canada = Nation("John Herdman", "Canada", "Jonathan David", "Scott Arfield", "Alphonso Davies", 2.5, 3.5)
        morocco = Nation("Vahid Halilhodžić", "Morocco", "Achraf Hakimi", "Hakim Ziyech", "Romain Saïss", 3.5, 4.5)
        croatia = Nation("Zlatko Dalić", "Croatia", "Ivan Perišić", "Luka Modrić", "Domagoj Vida", 4.5, 4.5)
        groupF = Group(belgium, canada, morocco, croatia)
        self.groups.append(groupF)
        
        # Group G
        brazil = Nation("Tite (Adenor Leonardo Bacchi)", "Brazil", "Neymar Jr.", "Casemiro", "Marquinhos", 5, 5)
        serbia = Nation("Dragan Stojković", "Serbia", "Dušan Tadić", "Sergej Milinković-Savić", "Aleksandar Kolarov", 3.5, 4)
        switzerland = Nation("Murat Yakin", "Switzerland",  "Xherdan Shaqiri", "Granit Xhaka","Manuel Akanji", 3.5, 3.5)
        cameroon = Nation("Toni Conceição", "Cameroon", "Eric Maxim Choupo-Moting", "André-Frank Zambo Anguissa", "Joël Matip", 4, 2.5)
        groupG = Group(brazil, serbia, switzerland, cameroon)
        self.groups.append(groupG)
        
        # Group H
        portugal = Nation("Fernando Santos", "Portugal", "Cristiano Ronaldo", "Bruno Fernandes", "Ruben Dias", 5, 5)
        ghana = Nation("Otto Addo", "Ghana", "Andre Ayew", "Thomas Partey", "Daniel Amartey", 3.5, 3.0)
        uruguay = Nation("Óscar Tabárez", "Uruguay", "Luis Suárez", "Federico Valverde", "José María Giménez", 4.5, 4.5)
        korea_republic = Nation("Paulo Bento", "Korea Republic", "Son Heung-min", "Hwang Hee-chan", "Kim Min-jae", 2.5, 2.5)
        groupH = Group(portugal, ghana, uruguay, korea_republic)
        self.groups.append(groupH)
        
    def simulate(self):
        for group in self.groups:
            group.simulateGamesCPU()
            
        self.quarterFinals()
        self.semiFinals()
        self.finals()
        return
        