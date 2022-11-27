from itertools import combinations

class Actions:

    TOKEN_TYPES = ['green', 'blue', 'red', 'white', 'black', 'yellow']
    POSSIBLE_ACTIONS = ['take_3', 'take_2', 'reserve', 'purchase', 'do_nothing']
    JOKER_COLOR = 'yellow'
    MIN_TOKEN_FOR_TAKE_2 = 4
    BOARD_X, BOARD_Y = (3, 4)
    MAX_RESERVED_CARDS = 3

    def get_subsets(li, size=3):
        return set(combinations(li, size))

    def get_possible_actions(self, player):
        actions = []
        
        # First type : take_3
        take_3 = self.game.POSSIBLE_ACTIONS[0]
        # Retrieve list of tokens minus the yellow ones (they cannot be picked)
        allowed_tokens = self.game.TOKEN_TYPES.copy()
        allowed_tokens.remove(self.game.JOKER_COLOR)
        available_tokens = set()
        # Check if there's still available tokens of each color
        for color in allowed_tokens:
            if self.state.still_has_token(color):
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
        take_2 = self.game.POSSIBLE_ACTIONS[1]
        for color in allowed_tokens:
            if self.state.tokens[color] >= self.game.MIN_TOKEN_FOR_TAKE_2:
                new_action = {
                    'type': take_2,
                    'params': color
                }
                actions.append(new_action)
        
        # Third type : reserve
        reserve = self.game.POSSIBLE_ACTIONS[2]
        if len(player.hand) < self.game.MAX_RESERVED_CARDS:
            # Pick a reserved cards from the middle of the table
            for i in range(self.game.BOARD_X):
                for j in range(self.game.BOARD_Y):
                    if self.state.cards[i][j].is_empty():
                        break
                    new_action = {
                        'type': reserve,
                        'params': ['from_table', (i, j)]
                        }
                    actions.append(new_action)
        
        # Fourth : buy a card
        purchase = self.game.POSSIBLE_ACTIONS[3]
        for i in range(self.game.BOARD_X):
            for j in range(self.game.BOARD_Y):
                if self.state.cards[i][j].is_empty():
                    break
                card = self.state.cards[i][j]
                if player.can_buy(card):
                    new_action = {
                        'type': purchase,
                        'params': ['from_table', (i, j)]
                    }
                    actions.append(new_action)
        for i in range(len(player.hand)):
            card = player.hand[i]
            if player.can_buy(card):
                new_action = {
                    'type': purchase,
                    'params': ['from_hand', i]
                }
                actions.append(new_action)
                
        # Else: do nothing
        if len(actions) == 0:
            do_nothing = self.game.POSSIBLE_ACTIONS[4]
            new_action = {
                'type': do_nothing,
                'params': None
                }
            actions.append(new_action)
            
        
        return(actions)




class Result:
    def ParseAction( gameState, action):
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
        

    def ReserveCard(self, gameState, card):
        gameState.RemoveCard(card)
        gameState.Reserve(gameState.GetTurn(), card)
        return gameState

    
    def PurchaseCard(self,gameState, card):
        gameState.RemoveCard(card)
        gameState.Purchase(gameState.GetTurn(), card)
        return gameState

