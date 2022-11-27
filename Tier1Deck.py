from individualCard import tier1Cards 
from deck import deck
class Tier1Deck(deck):

    def __init__(self):
        self._deck = [
            tier1Cards.card1, tier1Cards.card2, tier1Cards.card3, tier1Cards.card4, tier1Cards.card5, tier1Cards.card6, tier1Cards.card7, tier1Cards.card8, tier1Cards.card9, tier1Cards.card10,
            tier1Cards.card11, tier1Cards.card12, tier1Cards.card13, tier1Cards.card14, tier1Cards.card15, tier1Cards.card16, tier1Cards.card17, tier1Cards.card18, tier1Cards.card19, tier1Cards.card20,
            tier1Cards.card21, tier1Cards.card22, tier1Cards.card23, tier1Cards.card24, tier1Cards.card25, tier1Cards.card26, tier1Cards.card27, tier1Cards.card28, tier1Cards.card29, tier1Cards.card30,
            tier1Cards.card31, tier1Cards.card32, tier1Cards.card33, tier1Cards.card34, tier1Cards.card35, tier1Cards.card36, tier1Cards.card37, tier1Cards.card38, tier1Cards.card39, tier1Cards.card40
        ]
        
    @property
    def deck(self):
        return self._deck

    


