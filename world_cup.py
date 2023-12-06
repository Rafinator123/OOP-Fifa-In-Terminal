"""App file containing class definitions"""

class Nation:
    coach: str
    nation: str
    key_outfielder: str
    key_defender: str
    def __init__(self, c: str, n: str, o: str, d: str) -> None:
        self.coach = c
        self.nation = n
        self.key_outfielder = o
        self.key_defender = d
        pass
    
class Group:
    """Class containing each group where group has 4 nations that will play against each other"""
    firstPlace
    secondPlace
    group = {}
    def __init__(self,n1,n2,n3,n4) -> None:
        self.group["a"] = n1
        self.group["b"] = n2
        self.group["c"] = n3
        self.group["d"] = n4
        return
    def simulateGames():
        
class WorldCup:
    user: Nation
    Group groupA = Group("")
    def __init__(self):
        
        return
    def simulate():
        groupStage()
        quarterFinals()
        semiFinals()
        finals()
        return
        