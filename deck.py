import random
class deck:
    _deck = []

    def Shuffle(self):
        random.shuffle(self._deck)

    def RemoveFromDeck(self, card):
        if(card in self._deck):
            self._deck.remove(card)
