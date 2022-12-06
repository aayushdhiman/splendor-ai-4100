from card import card
class hand:
        
        def __init__(self):
                self.deck = []
                self.deckTokens = {'white': 0, 'blue': 0, 'green': 0, 'red': 0, 'black': 0}
                self.token : dict = {'white': 0, 'blue': 0, 'green': 0, 'red': 0, 'black': 0}
                self.prestigePoint : int= 0

        def copy(self):
                newHand = hand()
                
                for key,value in self.token.items():
                        newHand.token.update({key:value}) 
                newHand.deck = [card for card in self.deck]                
                newHand.prestigePoint = self.prestigePoint
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

        def AddCard(self, card : card):
                self.deck.append(card)
                self.deckTokens[card.color] += 1
                self.prestigePoint += card.prestige

        def ReserveCard(self, card):
                self.reservePile.append(card)

        def CanBuy(self, potentialCard : card):
                cost : dict = potentialCard.cost
                for mineral, amount in cost.items():
                        if(self.token[mineral] + self.deckTokens[mineral] < amount):
                                return False
                return True



 
