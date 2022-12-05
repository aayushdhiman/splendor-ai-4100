from card import card
class hand:
        
        def __init__(self):
                self.deck = []
                self.reservePile = []
                self.token : dict = {'white': 0, 'blue': 0, 'green': 0, 'red': 0, 'black': 0}
                self.prestigePoint = 0

        def copy(self):
                deckCopy = [card for card in self.deck]
                reservePileCopy = [card for card in self.reservePile]
                tokenCopy = {}
                for key,value in self.token:
                        tokenCopy.update({key:value}) 
                newHand = hand()
                newHand.deck = deckCopy
                newHand.token = tokenCopy
                newHand.prestigePoint = self.prestigePoint
                newHand.reservePile = reservePileCopy
                return newHand       

        def getDeck(self):
                return self.deck
        
        def getPrestige(self):
                return self.prestigePoint

        def getNumTokens(self):
                ans = 0
                for aToken in self.getTokens().values():
                        ans += aToken
                return ans

        def getTokens(self):
                return self.token

        def AddCard(self, card):
                self.deck.append(card)
                self.prestigePoint += card.prestige

        def ReserveCard(self, card):
                self.reservePile.append(card)

        def CanBuy(self, potentialCard : card):
                cost : dict = potentialCard.cost
                for mineral, amount in cost.items():
                        if(self.token[mineral] < amount):
                                return False
                return True



 
