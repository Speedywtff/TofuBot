import random

class DefineCards:
    def __init__(self, numJokers = 0, replace = False):
        self.suites = ["spades", "hearts", "diamonds", "clubs"]
        self.val = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.numJokers = numJokers
        self.bannedPairs = {"spades": [], "hearts": [], "diamonds": [], "clubs": [], "jokersUsed": 0}
        self.deck = {}
        self.replace = replace

    def getRandomCard(self):
        if self.numJokers > 0:
            if self.replace == True:
                choices = self.val + ["J" for i in range(self.numJokers)]
                Card = random.choice(choices)
                if Card != "J":
                    return {"suite": random.choice(self.suites), "value": Card}
                else:
                    return {"suite": "Null", "value": "J"}
            else:
                flag = True
                while flag:
                    choices = self.val + ["J" for i in range(self.numJokers)]
                    Card = random.choice(choices)
                    if Card != "J":
                        suiteChoice = random.choice(self.suites)
                        for banned in self.bannedPairs[suiteChoice]:
                            if banned == Card:
                                continue
                        self.bannedPairs[suiteChoice].append(Card)
                        return {"suite": suiteChoice, "value": Card}
                    else:
                        if self.bannedPairs["jokersUsed"] == self.numJokers:
                            continue
                        else:
                            self.bannedPairs["jokersUsed"] += 1
                            return {"suite": "Null", "value": "J"}
                            
        else:
            if self.replace == False:
                flag = True
                while flag:
                    Card = random.choice(self.val)  
                    suite =  random.choice(self.suites)
                    for banned in self.bannedPairs[suite]:
                        if banned == Card:
                            continue
                    return {"suite": suite, "value": Card}
            else:
                Card = random.choice(self.val)  
                suite =  random.choice(self.suites)
                return {"suite": suite, "value": Card}
    
    def getBannedCards(self):
        return self.bannedPairs
        

            



