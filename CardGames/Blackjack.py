from DefineCards import DefineCards

class Blackjack(DefineCards):
    def __init__(self, player = True):
        super().__init__()
        self.values = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 0}
        self.deck = []
        self.total = 0
        self.player = player
        self.lost = False
    

    def peek(self):
        if self.player:
            return self.deck
        else:
            return None 
    
    def checkTotal(self):
        return self.total
    
    def calcTotal(self):
        total = 0
        for i in self.deck:
            val = self.values[i]
            if i != 'Ace':
                total += val
                self.total = total
            else:
                if total + 11 <= 21:
                    total += 11
                    self.values["Ace"] = 11
                    self.total = total
                elif total + 1 <= 21:
                    total += 1
                    self.values["Ace"] = 1
                    self.total = total
                else:
                    self.lost = True
                    return False
    
    def getCard(self):
        Card = DefineCards().getRandomCard()
        self.deck.append(Card["value"])
    
    def isLost(self):
        return self.lost

    

