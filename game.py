from hand import hand
from state import state
from itertools import combinations
from screen import graphics

import Tier1Deck 
import Tier2Deck 
import Tier3Deck 
import ActionUtil


class game:

        def __init__(self):
                """
                
                """
                self.turns = True

                tier1deck = Tier1Deck.Tier1Deck()
                tier1deck.Shuffle()
                tier1Pool = []

                tier2deck = Tier2Deck.Tier2Deck()
                tier2deck.Shuffle()
                tier2Pool = []


                tier3deck = Tier3Deck.Tier3Deck()
                tier3deck.Shuffle()
                tier3Pool = []

                for card in tier1deck.deck[:3]:
                        tier1deck.RemoveFromDeck(card)
                        tier1Pool.append(card)

                        
                for card in tier2deck.deck[:3]:
                        tier2deck.RemoveFromDeck(card)
                        tier2Pool.append(card)

                for card in tier3deck.deck[:3]:
                        tier3deck.RemoveFromDeck(card)
                        tier3Pool.append(card)

                examplePlayerHand = hand()
                examplePlayerHand.AddCard(tier1deck.deck[5])

                self.gameState = state(
                        {
                                'white': 7, 'blue': 7, 'green': 7, 'red': 7, 'black': 7
                        },
                        [tier1Pool,tier2Pool,tier3Pool],
                        [[card for card in tier1deck.deck],
                        [card for card in tier2deck.deck],
                        [card for card in tier3deck.deck]],
                        examplePlayerHand,
                        hand()

                )
                self.gameOver = False
                self.display = graphics(self.gameState)
                self.display.showScreen()
                  


        def getGameState(self):
                return self.gameState
        
        def getTurns(self):
                return self.turns
        
        def updateTurns(self):
                self.turns = not self.turns

        def takeAction(self,action):
                self.gameState = self.gameState.ParseAction(action)

        
        

                

   

        def ParseAction(self, gameState, action):
          
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
        




        


newGame = game()

#print(newGame.get_possible_actions(newGame.gameState)[0])
#print(newGame.gameState.ParseAction(newGame.get_possible_actions(newGame.gameState)[0]))
# for action, gameState in newGame.getSuccessors(newGame.gameState):
#         print(gameState.eval())
        


