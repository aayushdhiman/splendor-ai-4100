from individualCard import tier3Card 
from deck import deck
class Tier3Deck(deck):

    def __init__(self):
        self._deck = [
            tier3Card.card1,tier3Card.card2, tier3Card.card3,tier3Card.card4, tier3Card.card5, tier3Card.card6, tier3Card.card7, tier3Card.card8, tier3Card.card9, tier3Card.card10,
            tier3Card.card11,tier3Card.card12,tier3Card.card13,tier3Card.card14,tier3Card.card15,tier3Card.card16,tier3Card.card17,tier3Card.card18,tier3Card.card19,tier3Card.card20,
        ]
        
    @property
    def deck(self):
        return self._deck

    


