from hand import hand 

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
                self.isPlayerTurn = True 

        def copy(self):
                return state(self.pool, self.table, self.deck1, self.deck2, self.deck3,self.playerHand.copy(), self.computerHand.copy())

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

        def ParseAction(self, action):

              
                print(action['type'])
             
                if action['type'] == 'take_3' or action['type'] == 'take_2':
                        print('UPDATED TOKENS')
                        successorGamestate = self.UpdateTokens(action['params'])
                elif action['type'] == 'reserve':
                        successorGamestate = self.ReserveCard(action['params'])
                elif action['type'] == 'purchase':
                        successorGamestate = self.PurchaseCard( action['params'])


                return successorGamestate
        
        def UpdateTokens(self, tokens):
                
                newGameState = self.copy()
                if(self.isPlayerTurn):
                        turnHand = newGameState.playerHand
                else:
                        turnHand = newGameState.computerHand

                for mineralType in tokens:
                        turnHand.token[mineralType] += 1
                        self.pool[mineralType] -= 1
                return newGameState
        

        def ReserveCard(self, origin, location):
                gameState = self.copy()
                if(origin == "from_table"):
                        card = gameState.GetCardAtTableLocation(location)
                        gameState.RemoveCardFromTable(card)
                        gameState.Reserve(self.turns, card)
                return gameState

        def PurchaseCard(self, card):
                gameState = self.copy()
                gameState.RemoveCardFromPool(card)
                gameState.Purchase(gameState.GetTurn(), card)
                return gameState

        def still_has_token(self,color):
                if(self.pool[color] > 0):
                        return True
                return False

                

        
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

