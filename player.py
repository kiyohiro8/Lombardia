

class Player:

    def __init__(self, name, hand, point, APNAP):
        self.name = name
        self.hand = hand
        self.point = point
        self.APNAP = APNAP

    def showinfo(self):
        print(self.point)
