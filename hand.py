
class hand:
        
        def __init__(self):
                self.deck = []
                self.reservePile = []
                self.token = {}
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

 