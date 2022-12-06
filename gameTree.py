<<<<<<< HEAD
import game
import ActionUtil

class node:

    def __init__(self, game : game, value : float, children : list, isMaxNode: bool):
        self.game = game
        self.value = value
        self.children = children
        self.isMaxNode = isMaxNode

        
        # if self.state.getTurns == True:
        #     self.isMaxNode = True
        #     for action in ActionUtil.get_possible_actions(self.getGame.getGameState.getComputerHand):
                
        # else:
        #     self.isMaxNode = False

        # if depth == 3:
        #     self.value = game.newGame.eval
        # else:
        #     if self.state.getTurns == True:
        #         self.value = self.getMaxChild.getValue
        #     else:
        #         self.value = self.getMinChild.getValue
        

        

        

    def getGame(self):
        return self.game

    def getChildren(self):
        return self.children

    def getValue(self):
        return self.value

    def getIsMaxNode(self):
        return self.isMaxNode

    def getMaxChild(self):
        ans = float('-inf')
        for child in self.getChildren:
            if child.getValue >= ans:
                ans = child.getValue
        return ans

    def getMinChild(self):
        ans = float('inf')
        for child in self.getChildren:
            if child.getValue <= ans:
                ans = child.getValue
        return ans
    


    def setValue(self, num):
        self.value = num

rootNode = node(
    game.newGame,
    None,
    [],
    game.newGame.
)
    
=======
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
>>>>>>> 2e9a64bfb55eab92c28f8ac74c9ee839991ad276
