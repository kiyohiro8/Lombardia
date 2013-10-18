

class Player:

    def __init__(self, name, ptype, hand, point, APNAP):
        
        self.name = name
        self.ptype = ptype
        self.hand = hand
        self.point = point
        self.APNAP = APNAP

    def showinfo(self):
        print(self.point)

class cpu(Player):

    def __init__(self, name, ptype, hand, point, APNAP, state):
        Player.__init__(self, name, ptype, hand, point, APNAP)
        self.state = state
