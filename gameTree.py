import state
import game

class expectimax():

        def __init__(self, game, state) -> None:
                self.game = game
                self.state = state

        def expectimax(self):
                possible_actions = self.game.get_possible_actions(self.state)
                action_util_pairs = {}
                for action in possible_actions:
                        action_util_pairs[action] = self.state.eval(self.state.ParseAction(action))
                return max(action_util_pairs)
        
        


