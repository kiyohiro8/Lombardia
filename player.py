

class Player:

    def __init__(self, name, ptype, hand, point, APNAP, reveal):
        
        self.name = name
        self.ptype = ptype
        self.hand = hand
        self.point = point
        self.APNAP = APNAP
        self.reveal = reveal

    def showinfo(self):
        print("%s 手札:%i枚 勝利点: %i点" %(self.name, len(self.hand), self.point)

class cpu(Player):

    def __init__(self, name, ptype, hand, point, APNAP, reveal, state):
        Player.__init__(self, name, ptype, hand, point, APNAP)
        self.state = state
