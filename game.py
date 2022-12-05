from hand import hand
from state import state
from itertools import combinations

import Tier1Deck 
import Tier2Deck 
import Tier3Deck 


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
                        [card for card in tier1deck.deck],
                        [card for card in tier2deck.deck],
                        [card for card in tier3deck.deck],
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
                self.gameState = self.gameState.ParseAction(action)

        
        def isOver(self, gameState):
                if gameState.getPlayerhand.getPrestige >= 15 or \
                        gameState.getComputerHand.getPrestige >= 15:
                        self.gameOver = True

        TOKEN_TYPES = ['green', 'blue', 'red', 'white', 'black', 'yellow']
        POSSIBLE_ACTIONS = ['take_3', 'take_2', 'reserve', 'purchase', 'do_nothing']
        JOKER_COLOR = 'yellow'
        MIN_TOKEN_FOR_TAKE_2 = 4
        BOARD_X, BOARD_Y = (3, 4)
        MAX_RESERVED_CARDS = 3

        def get_subsets(self, li, size=3):
                return set(combinations(li, size))

        def get_possible_actions(self, gamestate : state):
                actions = []
                if(self.turns):
                        player : hand = gamestate.playerHand
                else:
                        player : hand = gamestate.computerHand

                # First type : take_3
                take_3 = self.POSSIBLE_ACTIONS[0]
                # Retrieve list of tokens minus the yellow ones (they cannot be picked)
                allowed_tokens = self.TOKEN_TYPES.copy()
                allowed_tokens.remove(self.JOKER_COLOR)
                available_tokens = set()
                # Check if there's still available tokens of each color
                for color in allowed_tokens:
                        if gamestate.still_has_token(color):
                                available_tokens.add(color)
                # Get all 3-tuples of available tokens
                all_token_tuples = self.get_subsets(available_tokens, 3)
                # Add them to the list of possible actions
                for token_tuple in all_token_tuples:
                        new_action = {
                        'type': take_3,
                        'params': token_tuple
                        }
                        actions.append(new_action)

                # Second type : take_2
                take_2 = self.POSSIBLE_ACTIONS[1]
                for color in allowed_tokens:
                        if gamestate.pool[color] >= self.MIN_TOKEN_FOR_TAKE_2:
                                new_action = {
                                        'type': take_2,
                                        'params': color
                                }
                                actions.append(new_action)

                # Third type : reserve
                reserve = self.POSSIBLE_ACTIONS[2]
                if len(player.getDeck()) < self.MAX_RESERVED_CARDS:
                        # Pick a reserved cards from the middle of the table
                        for i in range(self.BOARD_X):
                                for j in range(self.BOARD_Y):
                                        if gamestate.GetCardAtTableLocation([i,j]) != None:
                                                break
                                        new_action = {
                                        'type': reserve,
                                        'params': ['from_table', (i, j)]
                                        }
                                        actions.append(new_action)

                # Fourth : buy a card
                purchase = self.POSSIBLE_ACTIONS[3]
                for i in range(self.BOARD_X):
                        for j in range(self.BOARD_Y):
                                if gamestate.GetCardAtTableLocation([i,j]) != None:
                                        break
                                card = gamestate.GetCardAtTableLocation(i,j)
                                if player.CanBuy(card):
                                        new_action = {
                                        'type': purchase,
                                        'params': ['from_table', (i, j)]
                                        }
                                        actions.append(new_action)
                for i in range(len(player.deck)):
                        card = player.deck[i]
                        if player.CanBuy(card):
                                new_action = {
                                        'type': purchase,
                                        'params': ['from_hand', i]
                                }
                                actions.append(new_action)
                                
                # Else: do nothing
                if len(actions) == 0:
                        do_nothing = self.POSSIBLE_ACTIONS[4]
                        new_action = {
                        'type': do_nothing,
                        'params': None
                        }
                        actions.append(new_action)
                        

                return(actions)

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


newGame = game()
print(newGame.gameState)
print(newGame.get_possible_actions(newGame.gameState,))