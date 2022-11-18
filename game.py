import card
import individualCard
import gameState

class game:

        def __init__(self, gameState):
                """
                
                """
                self.truns = True
                self.gameState = state
                self.gameOver = False


        def getGameState(self):
                return self.gameState
        
        def getTurns(self):
                return self.truns
        
        def updateTurns(self):
                self.turns = not self.turns

        
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