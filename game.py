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

                examplePlayerHand = hand()
                examplePlayerHand.AddCard(tier1deck.deck[5])

                self.gameState = state(
                        {
                                'white': 7, 'blue': 7, 'green': 7, 'red': 7, 'black': 7
                        },
                        [tier1Pool,tier1Pool,tier1Pool],
                        [card for card in tier1deck],
                        [card for card in tier1deck],
                        [card for card in tier1deck],
                        examplePlayerHand,
                        hand()

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

        def getWinLoss(self):
                ans = 0
                if self.getGameState().getComputerHand().getPrestige() >= 15:
                        ans = 1
                if self.getGameState().getPlayerHand().getPrestige() >= 15:
                        ans = -1
                return ans

        def ParseAction(self, gameState, action):
                action =  {
                'type': 'aaa',
                'params': 'tokens'
                }
                if action['type'] == 'take_3' or action['type'] == 'take_2':
                        gameState = self.UpdateTokens(gameState, action['params'])
                elif action['type'] == 'reserve':
                        gameState = self.ReserveCard(gameState, action['params'])
                elif action['type'] == 'purchase':
                        gameState = self.PurchaseCard(gameState, action['params'])
                else:
                        gameState = gameState

                return gameState
        
        def UpdateTokens(self, gameState, tokens):
                for token in tokens:
                        gameState.AddToken(token)
                return gameState
        

        def ReserveCard(self, gameState, origin, location):
                
                if(origin == "from_table"):
                        card = gameState.GetCardAtTableLocation(location)
                        gameState.RemoveCardFromTable(card)
                        gameState.Reserve(self.turns, card)
                return gameState

        def PurchaseCard(self,gameState, card):
                gameState.RemoveCardFromPool(card)
                gameState.Purchase(gameState.GetTurn(), card)
                return gameState

        def eval(self):
                ans = 100 * self.getWinLoss() + 2 * self.getGameState().getComputerHand().getPrestige() + len(self.getGameState().getComputerHand().getDeck()) + self.getGameState().getComputerHand().getNumTokens()
                return ans   


class hand:
        
        def __init__(self):
                self.deck = []
                self.reservePile = []
                self.token = {}
                self.prestigePoint = 0

        
        def getDeck(self):
                return self.deck
        
        def getPrestige(self):
                return self.prestigePoint

        def getNumTokens(self):
                ans = 0
                for aToken in self.getTokens():
                        ans += aToken.num
                return ans

        def getTokens(self):
                return self.token

        def AddCard(self, card):
                self.deck.append(card)
                self.prestigePoint += card.prestige

        def ReserveCard(self, card):
                self.reservePile.append(card)

 

class state:

        def __init__(self, pool : dict, table : list, deck1 : list, deck2 : list, deck3 : list, playerHand : hand, computerHand : hand):
                """
                
                """
                self.pool = pool
                self.table = table
                self.deck1 = deck1
                self.deck2 = deck2
                self.deck3 = deck3
                self.playerHand = playerHand
                self.computerHand = computerHand


        def getPool(self):
                return self.pool

        def generatePool(self):
                pass
        
        def getPlayerHand(self):
                return self.playerHand

        def getComputerHand(self):
                return self.computerHand

        def GetCardAtTableLocation(self, location):
                if(location[0] == 0):
                        return self.deck1[location[1]]
                if(location[0] == 1):
                        return self.deck2[location[1]]
                if(location[0] == 2):
                        return self.deck3[location[1]]


        
        def __repr__(self):
                return "Current Game State: \n\n" + "Current Pool: " + \
                        "\n     White: " + str(self.pool['white']) + \
                        "\n     Blue: " + str(self.pool['blue']) + \
                        "\n     Green: " + str(self.pool['green']) + \
                        "\n     Red: " + str(self.pool['red']) + \
                        "\n     Black: " + str(self.pool['black']) + \
                        "\n\nCurrent Table: " + \
                        "\n     Tier 1: " + " ".join(["\n       " +str(card) for card in self.table[0]]) +  \
                        "\n     Tier 2: " + " ".join(["\n       " +str(card) for card in self.table[1]])   + \
                        "\n     Tier 3: " + " ".join(["\n       " + str(card) for card in self.table[2]]) + \
                        "\n\nPlayer hand:" + "".join(["\n       " + str(card) for card in self.playerHand.getDeck()]) + "\n       Current Prestige:" + str(self.playerHand.getPrestige()) + \
                        "\n\nComputer hand:" + "".join(["\n       " + str(card) for card in self.computerHand.getDeck()]) + "\n       Current Prestige:" + str(self.computerHand.getPrestige()) 


newGame = game()
print(newGame.gameState)