from hand import hand 
from itertools import combinations
import random
from card import card

class state:
        TOKEN_TYPES = ['green', 'blue', 'red', 'white', 'black', 'yellow']
        POSSIBLE_ACTIONS = ['take_3', 'take_2', 'reserve', 'purchase', 'do_nothing']
        JOKER_COLOR = 'yellow'
        MIN_TOKEN_FOR_TAKE_2 = 4
        BOARD_X, BOARD_Y = (3, 4)
        MAX_RESERVED_CARDS = 3

        def __init__(self, pool : dict, table : list, deck : list, playerHand : hand, computerHand : hand):
                """
                
                """
                self.pool = pool
                self.table = table
                self.deck = deck
                self.playerHand = playerHand
                self.computerHand = computerHand
                self.isPlayerTurn = False
                

        def copy(self):
                return state(self.pool, self.table, self.deck, self.playerHand.copy(), self.computerHand.copy())

        def getPool(self):
                return self.pool

        def generatePool(self):
                pass
        
        def getPlayerHand(self):
                return self.playerHand

        def getComputerHand(self):
                return self.computerHand

        def GetCardAtTableLocation(self, location):
                return self.deck[location[0]][location[1]]
              

        def ParseAction(self, action):

              
          
                if action['type'] == 'take_3' or action['type'] == 'take_2':
                        successorGamestate = self.UpdateTokens(action['params'])
                elif action['type'] == 'purchase':
                        successorGamestate = self.PurchaseCard( action['params'])


                return successorGamestate
        
        def UpdateTokens(self, tokens):
                
                newGameState = self.copy()
                if(self.isPlayerTurn):
                        turnHand = newGameState.playerHand
                else:
                        turnHand = newGameState.computerHand
                if(type(tokens) == tuple):
                        for mineralType in tokens:
                                turnHand.token[mineralType] += 1
                                self.pool[mineralType] -= 1
                else:
                        turnHand.token[tokens] += 2
                return newGameState
        


        def PurchaseCard(self, card):
                gameState : state = self.copy()
                gameState.ReplaceCardFromPool(card)
                gameState.Purchase(card)
                return gameState

        def GetLocationOfCard(self,card):
                for pool, index in enumerate(self.pool):
                        for newCard, cardInex in enumerate(pool):
                                if(card == newCard):
                                        return [index, cardInex]

        def ReplaceCardFromPool(self, card):
                poolIndex,cardIndex = self.GetLocationOfCard(card)
                newCard = random.choice(self.deck[poolIndex])
                self.pool[poolIndex][cardIndex] = newCard
                self.deck[poolIndex].remove(newCard)

        def Purchase(self, chosenCard : card):
                if(self.isPlayerTurn):
                        turnHand = self.playerHand
                else:
                        turnHand = self.computerHand
                for mineralType, cost in chosenCard.cost:
                        turnHand.token[mineralType] -= cost
                
                turnHand.AddCard(chosenCard)


        def still_has_token(self,color):
                if(self.pool[color] > 0):
                        return True
                return False
        def eval(self):
                ans = 100 * self.getWinLoss() + 2 * self.getComputerHand().getPrestige() + len(self.getComputerHand().getDeck()) + self.getComputerHand().getNumTokens() - 2 * self.getPlayerHand().getPrestige() - len(self.getPlayerHand().getDeck()) - self.getPlayerHand().getNumTokens()
                return ans   
                
        def getWinLoss(self):
                ans = 0
                if self.getComputerHand().getPrestige() >= 15:
                        ans = 1
                if self.getPlayerHand().getPrestige() >= 15:
                        ans = -1
                return ans

        def isOver(self):
                return self.getPlayerhand.getPrestige >= 15 or \
                        self.getComputerHand.getPrestige >= 15
       


        def get_subsets(self, li, size=3):
                return set(combinations(li, size))

        def get_possible_actions(self):
                actions = []
                if(self.isPlayerTurn):
                        player : hand = self.playerHand
                else:
                        player : hand = self.computerHand

                # First type : take_3
                take_3 = self.POSSIBLE_ACTIONS[0]
                # Retrieve list of tokens minus the yellow ones (they cannot be picked)
                allowed_tokens = self.TOKEN_TYPES.copy()
                allowed_tokens.remove(self.JOKER_COLOR)
                available_tokens = set()
                # Check if there's still available tokens of each color
                for color in allowed_tokens:
                        if self.still_has_token(color):
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
                        if self.pool[color] >= self.MIN_TOKEN_FOR_TAKE_2:
                                new_action = {
                                        'type': take_2,
                                        'params': color
                                }
                                actions.append(new_action)

                # third : buy a card
                purchase = self.POSSIBLE_ACTIONS[3]
                for i in range(self.BOARD_X):
                        for j in range(self.BOARD_Y):
                                if self.GetCardAtTableLocation([i,j]) != None:
                                        break
                                card = self.GetCardAtTableLocation(i,j)
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

        def getSuccessors(self):
                successor = []
                for action in self.get_possible_actions():
                        successor.append([action, self.ParseAction(action)])

                return successor

        def getSuccessor(self, action):
                return [action, self.ParseAction(action)]

                

        
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

