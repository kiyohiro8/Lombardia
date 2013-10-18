

class Player:

    def __init__(self, name, ptype, hand, point, APNAP):
        
        self.name = name
        self.type = ptype
        self.hand = hand
        self.point = point
        self.APNAP = APNAP

    def showinfo(self):
        print(self.point)
