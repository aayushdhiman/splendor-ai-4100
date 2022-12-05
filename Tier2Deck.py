from individualCard import tier2Card 
from deck import deck
class Tier2Deck(deck):

    def __init__(self):
        self._deck = [
            tier2Card.card1,tier2Card.card2, tier2Card.card3,tier2Card.card4, tier2Card.card5, tier2Card.card6, tier2Card.card7, tier2Card.card8, tier2Card.card9, tier2Card.card10,
            tier2Card.card11,tier2Card.card12,tier2Card.card13,tier2Card.card14,tier2Card.card15,tier2Card.card16,tier2Card.card17,tier2Card.card18,tier2Card.card19,tier2Card.card20,
            tier2Card.card21,tier2Card.card22,tier2Card.card23,tier2Card.card24,tier2Card.card25,tier2Card.card26,tier2Card.card27,tier2Card.card28,tier2Card.card29,tier2Card.card30,
        ]
        
    @property
    def deck(self):
        return self._deck

    


