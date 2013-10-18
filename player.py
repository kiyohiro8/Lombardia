

class Player:

    def __init__(self, name, ptype, hand, point, APNAP):
        
        self.name = name
        self.ptype = ptype
        self.hand = hand
        self.point = point
        self.APNAP = APNAP

    def showinfo(self):
        print(self.point)

class ptype(Player):

    def __init__(state):
        self.state = state
