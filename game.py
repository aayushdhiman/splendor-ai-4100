import Tier1Deck 
 
import ActionUtil
from ActionUtil import Result

class game:

        def __init__(self):
                """
                
                """
                self.turns = True

                tier1deck = Tier1Deck.Tier1Deck()
                tier1deck.Shuffle()
                tier1Pool = []
                for card in tier1deck.deck[:3]:
                        tier1deck.RemoveFromDeck(card)
                        tier1Pool.append(card)

                self.gameState = state(
                        {
                                'white': 7, 'blue': 7, 'green': 7, 'red': 7, 'black': 7
                        },
                        [tier1Pool,tier1Pool,tier1Pool],
                        tier1deck,
                        tier1deck,
                        tier1deck,
                        [],
                        []

                )
                self.gameOver = False
                  


        def getGameState(self):
                return self.gameState
        
        def getTurns(self):
                return self.turns
        
        def updateTurns(self):
                self.turns = not self.turns

        def takeAction(self,action):
                Result.ParseAction(self.gameState, action)

        
        def isOver(self, gameState):
                if gameState.getPlayerhand.getPrestige >= 15 or \
                        gameState.getComputerHand.getPrestige >= 15:
                        self.gameOver = True
 
                



class state:

        def __init__(self, pool, table, deck1, deck2, deck3, playerHand, computerHand):
                """
                
                """
                self.pool = pool
                self.table = table
                self.deck1 = deck1
                self.deck2 = deck2
                self.deck3 = deck3
                self.playerHand = hand
                self.computerHand = hand


        def getPool(self):
                return self.pool

        def generatePool(self):
                pass
        
        def getPlayerHand(self):
                return self.playerHand

        def getComputerHand(self):
                return self.computerHand

        
        def __repr__(self):
                return "Current Game State: \n\n" + "Current Pool: " + \
                        "\n     White: " + str(self.pool['white']) + \
                        "\n     Blue: " + str(self.pool['blue']) + \
                        "\n     Green: " + str(self.pool['green']) + \
                        "\n     Red: " + str(self.pool['red']) + \
                        "\n     Black: " + str(self.pool['black']) + \
                        "\n\nCurrent Table: " + \
                        "\n     Tier 1: " + " ".join([str(card) for card in self.table[0]]) +  \
                        "\n     Tier 2: " + " ".join([str(card) for card in self.table[1]])   + \
                        "\n     Tier 3: " + " ".join([str(card) for card in self.table[2]]) 


class hand:
        
        def __init__(self):
                self.deck = {}
                self.token = {}
                self.prestigePoint = 0

        
        def getDeck(self):
                return self.deck
        
        def getPrestige(self):
                return self.prestigePoint


        def updateHand(self, action):
                pass
              
newGame = game()
print(newGame.gameState)