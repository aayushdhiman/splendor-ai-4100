import state
import game
import sys

class expectimax():

        def __init__(self, game, state) -> None:
                #self.depth = depth
                self.game = game
                self.state = state

        # def expectimax(self):

        #         possible_actions = self.game.get_possible_actions(self.state)
        #         action_util_pairs = {}
        #         for action in possible_actions:
        #                 action_util_pairs[action] = self.state.eval(self.state.ParseAction(action))
        #         return max(action_util_pairs)
        

        def getAction(self):
            """
            Returns the expectimax action using self.depth and self.evaluationFunction

            All ghosts should be modeled as choosing uniformly at random from their
            legal moves.
            """
            "*** YOUR CODE HERE ***"

            value, move = self.max_value(self.state, 0)
            return move

        def value(self, state, depth):


            # end case scenarios
            if state.isOver() or depth >= 3:
                return state.eval()

            # determine min turn or max turn
            if depth % 2 == 0:
                value, move = self.max_value(game, depth+1)
            else:
                value, move = self.min_value(game, depth+1)

            return value

        def max_value(self, state, depth):


            NEGINF = -sys.maxsize-1
            cur = (NEGINF, '')

            for action in state.get_possible_actions():
                nex = (self.value(state.getSuccessor(action), depth + 1), action)
                cur = nex if cur[0] <= nex[0] else cur

            return cur

        def min_value(self, state, depth):
        

            # expect value
            exp = 0

            # all possible moves
            actions = list(state.get_possible_actions())

            for action in actions:
                nex = (self.value(state.getSuccessor(action), depth + 1), action)
                exp += nex[0]

            exp /= len(actions)

            return (exp, '')
